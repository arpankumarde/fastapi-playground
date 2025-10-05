from fastapi import FastAPI
import database_models
from models import Product
from database import session, engine


app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

products = [
    Product(
        id=1,
        name="Eco Water Bottle",
        description="Durable, BPA-free, perfect for daily use.",
        price=57,
        quantity=23,
    ),
    Product(
        id=2,
        name="Bluetooth Speaker",
        description="Portable with 12 h battery life and deep bass.",
        price=112,
        quantity=8,
    ),
    Product(
        id=3,
        name="Yoga Mat",
        description="Non-slip surface, extra thick for comfort.",
        price=34,
        quantity=61,
    ),
    Product(
        id=4,
        name="Wireless Mouse",
        description="Ergonomic design with adjustable DPI.",
        price=78,
        quantity=15,
    ),
    Product(
        id=5,
        name="Stainless Steel Cookware Set",
        description="12-piece set, oven-safe, induction compatible.",
        price=149,
        quantity=42,
    ),
]


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


def init_db():
    db = session()
    count = db.query(database_models.Product).count

    if count == 0:
        for p in products:
            db.add(database_models.Product(**p.model_dump()))

    db.commit()


init_db()


@app.get("/")
def hello():
    return "Server is running!"


@app.get("/product")
def get_all_products():
    return products


@app.get("/product/{id}")
def get_product_by_id(id: int):
    for p in products:
        if p.id == id:
            return p

    return "Product Not found"


@app.post("/product")
def add_product(p: Product):
    products.append(p)
    return p


@app.put("/product/{id}")
def update_product(id: int, p: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = p
            return p

    return "Product Not Found"


@app.delete("/product/{id}")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            products.pop(i)
            return "Product Deleted"

    return "Product Not Found"
