from fastapi import APIRouter

from .user import router as users_router
from user_service.app.core.config import settings

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(
    users_router,
    prefix=settings.api.v1.users,
)
