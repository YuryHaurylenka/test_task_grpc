import uvicorn
from fastapi import FastAPI, status
from starlette.responses import RedirectResponse

from .core import settings
from .views import router as api_v1_router

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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
