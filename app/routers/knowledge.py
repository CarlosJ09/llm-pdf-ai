from fastapi import APIRouter
from controllers.knowledge import train_model_via_pdf


knowledge_router = APIRouter()


@knowledge_router.get("/train_model/", tags=["train_model"])
async def train_model(file_url: str):
    return await train_model_via_pdf(file_url)
