from pinecone.grpc import PineconeGRPC as Pinecone
from config.pinecone import (
    PINECONE_DB_API_KEY,
    PINECONE_DB_INDEX_NAME,
    PINECONE_DB_INDEX_HOST,
    PINECONE_DB_EMBEDDING_MODEL,
)
from utils.pdf_processor import process_pdf


async def train_model_via_pdf(file_url: str) -> dict:
    """Convert PDF to text, generate embeddings, and store them in Pinecone."""

    try:
        pc = Pinecone(api_key=PINECONE_DB_API_KEY)
        index = pc.Index(PINECONE_DB_INDEX_NAME, PINECONE_DB_INDEX_HOST)

        pages = await process_pdf(file_url)

        if not pages:
            return {"error": "No text extracted from PDF."}

        texts = [p.page_content.strip() for p in pages]

        embeddings = pc.inference.embed(
            model=PINECONE_DB_EMBEDDING_MODEL,
            inputs=texts,
            parameters={"input_type": "passage", "truncate": "END"},
        )

        records = []
        for idx, (text, embedding) in enumerate(zip(texts, embeddings)):
            records.append(
                {
                    "id": f"vec_{idx}",
                    "values": embedding["values"],
                    "metadata": {"text": text},
                }
            )

        index.upsert(vectors=records, namespace="example-namespace")

        return {"message": "Embedding stored successfully"}
    except Exception as e:
        return {"error": f"Failed to train model: {str(e)}"}
