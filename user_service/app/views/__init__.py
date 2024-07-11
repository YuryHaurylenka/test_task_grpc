from fastapi import APIRouter

from user_service.app.core.config import settings
from .user import router as users_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(
    users_router,
    prefix=settings.api.v1.users,
)