import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from user_service.app.core.config import settings
from views import router as api_v1_router

app = FastAPI()
app.include_router(
    api_v1_router,
    prefix=settings.api.prefix,
)


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host=settings.run.host, port=settings.run.port)
