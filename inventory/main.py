from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel
from typing import List, Optional

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:3000"], allow_methods=["*"], allow_headers=["*"])

redis = get_redis_connection(
    host = "redis-19176.c60.us-west-1-2.ec2.cloud.redislabs.com",
    port = 19176,
    password = "M82SSvTVz295fHPHQR9eAqnytAEI7iUV",
    decode_responses = True
)

class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis

@app.get("/products")
def get_products():
    return [product_schema(pk) for pk in Product.all_pks()]

def product_schema(pk: str):
    product = Product.get(pk)
    return {
        "id": product.pk,
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity,
    }

@app.get("/products/{pk}")
def get_product(pk: str):
    return Product.get(pk)
    
@app.post("/products")
def create_product(product: Product):
    return product.save()

@app.delete("/products/{pk}")
def delete_product(pk: str):
    return Product.delete(pk)