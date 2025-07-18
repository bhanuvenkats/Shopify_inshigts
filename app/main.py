from fastapi import FastAPI
from app.routers import insights

app = FastAPI()
app.include_router(insights.router)