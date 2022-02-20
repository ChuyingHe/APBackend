from fastapi import FastAPI
import uvicorn
from app.infrastructure.database.db import config_db

api_tags = [
    {
        "name": "operation",
        "description": "opeerations"
    },
    {
        "name": "user",
        "description": "user oriented api"
    },
    {
        "name": "product",
        "description": "product related api"
    },
];

# FAKE DATA
products = [
    {
        "name": "Natural Koffee Peeling Seife",
        "ingredients": "Koffee",
        "aroma": "Natural mit Kaffee Aroma",
        "functionality": "Activieren dein Haut, peeling off die veraltete und tote Haut"
    },
    {
        "name": "Orange & Lime Seife",
        "ingredients": "Orangenschale, Limenschale",
        "aroma": "Natural mit Orange & Lime Aroma",
        "functionality": "Sehr frishe Geruche, gibt dir ein Sommerliche Gefühl"
    },
]

app = FastAPI(openapi_tags=api_tags)

# Operation -----------------------------------------------------
@app.get("/", tags=['operation'])
async def root():
    return {"message": "Backend is alive"}


# User -----------------------------------------------------
@app.get("/user", tags=['user'])
async def get_current_user():
    return {"login function is not done yet"}

# Product -----------------------------------------------------
@app.get("/products", tags=['product'])
async def get_all_products():
    test_db_connection()
    return products

def test_db_connection():
    print("🦐 test_db_connection")
    config_db()

if __name__=="__main__":
    test_db_connection()
    uvicorn.run(app, host="0.0.0.0", port=4000)