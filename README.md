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
3. Configure the environment variables for each microservice. Create a `.env` file in the root directory of each
   microservice with the following content:

   **EXAMPLE URL** for **user-service** :
    ```env
   DB_URL=postgresql://username:password@localhost:5432/user_service_db
    ```

   **order_service/.env example**:
    ```env
    DB_URL=postgresql://username:password@localhost:5432/order_service_db
    ```

4. Configure the environment variables docker-compose in test_task_grpc/.env

   **test_task_grpc/.env example** :
    ```env
   DB_URL_USER=postgresql+asyncpg://postgres:postgres@user_db:5432/user_db
   DB_URL_ORDER=postgresql+asyncpg://postgres:postgres@order_db:5432/order_db
    ```


5. Build and start the containers using Docker Compose:
    ```sh
    docker-compose up --build
   ```

6. At the first startup in each microservice it is necessary to create tables with alembic

- For User microservice
   ```sh
    cd user_service
    alembic upgrade head
    ```

- For Order microservice
   ```sh
    cd order_service
    alembic upgrade head
    ```

### Configuration

- **user-service** swagger should be accessible at `localhost:8000/docs`.
- **order-service** swagger should be accessible at `localhost:8001/docs`.

Logs will be visible in the terminal after successful startup.

## How the app works

- Each microservice has 6 endpoints(Get all (GET), Create (POST), Get one (GET), Update (PUT), Update partial (PATCH),
  Delete (DELETE).

*Order endpoints*
![Order endpoints](https://github.com/YuryHaurylenka/test_task_grpc/blob/develop/screens/endpoints_order.png)
*User endpoints*
![User endpoints](https://github.com/YuryHaurylenka/test_task_grpc/blob/develop/screens/endpoints_user.png)

- When an order is created, a message is sent to the server that the GetUser method on the grpc server with user_id in
  the request is called. If a user with this user_id exists, the server reports this user, otherwise it reports that
  no such user was found.

*Correct order creating*
![Correct order creating](https://github.com/YuryHaurylenka/test_task_grpc/blob/develop/screens/correct_order_create.png)
*Wrong order creating
![Wrong order creating](https://github.com/YuryHaurylenka/test_task_grpc/blob/develop/screens/wrong_order_create.png)