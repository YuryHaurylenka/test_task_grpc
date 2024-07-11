from fastapi import FastAPI, status
from starlette.responses import RedirectResponse

from user_service.app.core.config import settings
from user_service.app.views import router as api_v1_router

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
