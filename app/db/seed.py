from ..models import Product
from ..schemas import schema
from .session import session

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


def init_db():
    db = session()
    try:
        count = db.query(schema.Product).count()
        if count == 0:
            for p in products:
                db.add(schema.Product(**p.model_dump()))
            db.commit()
            print("DB Seeding complete")
    finally:
        db.close()
