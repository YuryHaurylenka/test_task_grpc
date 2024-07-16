import asyncio
import logging
from starlette.responses import RedirectResponse

from fastapi import FastAPI, status
import uvicorn
from .core import settings
from .views import router as api_v1_router
from shared.user_grpc.user_service import serve_grpc

app = FastAPI()
app.include_router(
    api_v1_router,
    prefix=settings.api.prefix,
)


@app.get(
    "/",
    include_in_schema=False,
    status_code=status.HTTP_301_MOVED_PERMANENTLY,
)
async def root():
    return RedirectResponse(url="/docs")


async def start_uvicorn():
    config = uvicorn.Config(
        "user_service.app.main:app", host="0.0.0.0", port=8000, reload=True
    )
    server = uvicorn.Server(config)
    await server.serve()


async def start_servers():
    grpc_task = asyncio.create_task(serve_grpc())
    uvicorn_task = asyncio.create_task(start_uvicorn())
    try:
        await asyncio.gather(grpc_task, uvicorn_task)
    except asyncio.CancelledError:
        logging.info("Shutdown signal received, canceling tasks.")
        grpc_task.cancel()
        uvicorn_task.cancel()
        try:
            await grpc_task
        except asyncio.CancelledError:
            logging.info("gRPC server canceled.")
        try:
            await uvicorn_task
        except asyncio.CancelledError:
            logging.info("Uvicorn server canceled.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(start_servers())
    except Exception as e:
        logging.error(f"Error running the servers: {e}")
    finally:
        logging.info("Servers stopped.")
