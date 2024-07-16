# Test Task: Python Microservices with gRPC

## Task Description

Develop two microservices in Python( FastAPI ) that communicate with each other using gRPC.

### Microservice 1: user-service

**Functionality:**
- Store user information (name, email, age).
- Provide an API for CRUD operations for User.

### Microservice 2: order-service

**Functionality:**

- Store order information (title, description, user ID).
- Provide an API for CRUD operations for Order.
- When creating an order, send user information to user-service with information of the user(if it exists).

## Setup Instructions

### Environment Setup

1. Make sure Docker is installed.

2. Clone the repository:
    ```sh
    git clone https://github.com/YuryHaurylenka/test_task_grpc
    cd test_task_grpc
    ```
3. Configure the environment variables for each microservice. Create a `.env` file in the root directory of each microservice with the following content:

   **EXAMPLE URL** for **user-service** :
    ```env
    DB_URL=postgresql://username:password@localhost:5432/user_service_db
    ```

   **EXAMPLE URL** for **order-service**:
    ```env
    DB_URL=postgresql://username:password@localhost:5432/order_service_db
    ```

4. Build and start the containers using Docker Compose:
    ```sh
    docker-compose up --build
    ```

### Configuration

- **user-service** should be accessible at `localhost:8000`.
- **order-service** should be accessible at `localhost:8001`.


