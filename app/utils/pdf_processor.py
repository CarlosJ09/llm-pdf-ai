from langchain_community.document_loaders import PyPDFLoader


async def process_pdf(file_path: str = None):
    loader = PyPDFLoader(file_path)
    pages = []
    async for page in loader.alazy_load():
        pages.append(page)

    return pages
