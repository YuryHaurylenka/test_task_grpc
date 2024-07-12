import asyncio
import logging
from starlette.responses import RedirectResponse

from fastapi import FastAPI, status
import uvicorn
from user_service.app.core.config import settings
from user_service.app.views import router as api_v1_router
from user_service.grpc.user_service import serve_grpc

app = FastAPI()
app.include_router(
    api_v1_router,
    prefix=settings.api.prefix,
)


@app.get(
    "/",
    include_in_schema=False,
    status_code=status.HTTP_308_PERMANENT_REDIRECT,
)
async def root():
    return RedirectResponse(url="/docs")


async def start_uvicorn():
    config = uvicorn.Config("main:app", host="0.0.0.0", port=8000, reload=True)
    server = uvicorn.Server(config)
    await server.serve()


async def start_servers():
    grpc_task = asyncio.create_task(serve_grpc())
    uvicorn_task = asyncio.create_task(start_uvicorn())
    await asyncio.gather(grpc_task, uvicorn_task)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(start_servers())
