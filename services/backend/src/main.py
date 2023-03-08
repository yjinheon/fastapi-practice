from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
from src.database.register import register_tortoise  
from src.database.config import TORTOISE_ORM 
from tortoise import Tortoise

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# enable schemas to read relationship between models
Tortoise.init_models(["src.database.models"], "models")  # NEW

register_tortoise(app=app, config=TORTOISE_ORM, generate_schemas=False)


@app.get("/")
def home():
    return "Hello, World!"
