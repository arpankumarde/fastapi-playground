from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .models import Product
from .schemas import schema
from .db import engine, get_db
from .db.seed import init_db
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
