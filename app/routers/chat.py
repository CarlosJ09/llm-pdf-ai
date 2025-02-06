from fastapi import APIRouter
from controllers.chat import get_chat_response


chatbot_router = APIRouter()


@chatbot_router.get("/chat/", tags=["chat"])
async def chat(prompt: str):
    return get_chat_response(prompt)
