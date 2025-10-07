# fastapi-playground

Minimal FastAPI example with SQLAlchemy and PostgreSQL.

## Prerequisites

- Python 3.10+
- PostgreSQL running and accessible
- [uv](https://docs.astral.sh/uv/) package manager

## Install

Install dependencies using uv:

```bash
uv sync
```

This will create a virtual environment and install all dependencies defined in `pyproject.toml`.

## Configure database

- Default DB URL is set in `database.py`:
  `postgresql://postgres:1234@localhost:5432/fastapi-play`
- Update that URL to match your PostgreSQL user/password/host/db or modify `database.py` before running.

## Run the app

```bash
uv run uvicorn app:app --reload
```

## Notes

- On startup the app runs `database_models.Base.metadata.create_all(...)` and `init_db()` to seed some example products.
- The API uses Pydantic models defined in `models.py` and SQLAlchemy models in `database_models.py`.
- Interactive API documentation (Swagger UI) is available at `http://localhost:8000/docs`

## API endpoints

- `GET` `/` -> health check
- `GET` `/product` -> list all products
- `GET` `/product/{id}` -> get product by id
- `POST` `/product` -> add product (JSON body matching models.Product)
- `PUT` `/product/{id}` -> update product (JSON body matching models.Product)
- `DELETE` `/product/{id}` -> delete product

## Example

```bash
curl http://localhost:8000/product
```
