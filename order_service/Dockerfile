FROM python:3.11.3

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry

RUN poetry install --no-root
COPY . /app/order_service
COPY . /app/shared

ENV PYTHONPATH=/app:/app/shared

CMD ["poetry", "run", "python", "-m", "order_service.app.main"]