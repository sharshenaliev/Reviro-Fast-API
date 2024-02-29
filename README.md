# Usage

An overview of the project.

## Env configuration

Create `.env` file and fill data:

```shell
POSTGRES_DB=test
POSTGRES_USER=test
POSTGRES_PASSWORD=test
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
```

## Instructions on how to build and run your application using Docker Compose

1. Run Docker Compose command:

    ```
    docker-compose up -d --build
    ```
   
2. Run Unit tests:

    ```
    docker-compose exec app pytest
    ```

## Work with app

1. Swagger UI `http://localhost:8000/docs`.

2. ReDoc `http://localhost:8000/redoc`.

3. Admin panel `http://localhost:8000/admin`. 
