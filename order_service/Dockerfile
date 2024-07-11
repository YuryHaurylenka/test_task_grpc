FROM python:3.11.3

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry

RUN poetry install --no-root

COPY . /app/order_service

ENV PYTHONPATH=/app

CMD ["poetry", "run", "uvicorn", "order_service.app.main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
