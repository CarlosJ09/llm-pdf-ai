from fastapi import FastAPI
from routers.chat import chatbot_router
from routers.knowledge import knowledge_router

app = FastAPI()
app.include_router(chatbot_router)
app.include_router(knowledge_router)
