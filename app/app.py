from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .models import Product
from .schemas import schema
from .db import session, engine
from sqlalchemy.orm import Session


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

schema.Base.metadata.create_all(bind=engine)

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
    count = db.query(schema.Product).count

    if count == 0:
        for p in products:
            db.add(schema.Product(**p.model_dump()))

    db.commit()


init_db()


@app.get("/")
def hello():
    return "Server is running!"


@app.get("/product")
def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(schema.Product).all()
    return db_products


@app.get("/product/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(schema.Product).filter(schema.Product.id == id).first()

    if db_product:
        return db_product

    return "Product Not found"


@app.post("/product")
def add_product(p: Product, db: Session = Depends(get_db)):
    db.add(schema.Product(**p.model_dump()))
    db.commit()
    return p


@app.put("/product/{id}")
def update_product(id: int, p: Product, db: Session = Depends(get_db)):
    db_product = db.query(schema.Product).filter(schema.Product.id == id).first()

    if db_product:
        db_product.name = p.name
        db_product.description = p.description
        db_product.price = p.price
        db_product.quantity = p.quantity

        db.commit()
        db.refresh(db_product)
        return db_product
    else:
        return "Product Not Found"


@app.delete("/product/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(schema.Product).filter(schema.Product.id == id).first()

    if db_product:
        db.delete(db_product)
        db.commit()
    else:
        return "Product Not Found"
