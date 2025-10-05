# fastapi-playground

Minimal FastAPI example with SQLAlchemy and PostgreSQL.

Prerequisites

- Python 3.10+
- PostgreSQL running and accessible

Install

- Create a virtual environment and install requirements:
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  ```

Configure database

- Default DB URL is set in `database.py`:
  `postgresql://postgres:1234@localhost:5432/fastapi-play`
- Update that URL to match your PostgreSQL user/password/host/db or modify `database.py` before running.

Run the app

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

Notes

- On startup the app runs `database_models.Base.metadata.create_all(...)` and `init_db()` to seed some example products.
- The API uses Pydantic models defined in `models.py` and SQLAlchemy models in `database_models.py`.

API endpoints

- GET / -> health check
- GET /product -> list all products
- GET /product/{id} -> get product by id
- POST /product -> add product (JSON body matching models.Product)
- PUT /product/{id} -> update product (JSON body matching models.Product)
- DELETE /product/{id} -> delete product

Example

```bash
curl http://localhost:8000/product
```
