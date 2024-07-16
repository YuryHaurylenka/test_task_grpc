from fastapi import APIRouter, Depends, status
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from order_service.app.core import db_helper
from order_service.app.crud import order as crud_order
from order_service.app.dependencies import order_by_id
from order_service.app.errors import (
    handle_database_error,
    handle_integrity_error,
    handle_unexpected_error,
    handle_user_not_found_error,
)
from order_service.app.schemas import (
    Order,
    OrderCreate,
    OrderUpdate,
    OrderUpdatePartial,
)
from shared.order_grpc.grpc_client import check_user_exists

router = APIRouter(tags=["Orders"])


@router.get("/", response_model=list[Order])
async def get_orders(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    try:
        return await crud_order.get_orders(session=session)
    except SQLAlchemyError:
        handle_database_error()


@router.post("/", response_model=Order, status_code=status.HTTP_201_CREATED)
async def create_order(
    order_in: OrderCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    user_exists = await check_user_exists(order_in.user_id)
    if not user_exists:
        handle_user_not_found_error("User with the requested user_id not found")

    try:
        return await crud_order.create_order(session=session, order_in=order_in)
    except IntegrityError:
        handle_integrity_error()
    except SQLAlchemyError:
        handle_database_error()
    except Exception as e:
        handle_unexpected_error("An unexpected error occurred while creating the order")


@router.get("/{order_id}/", response_model=Order)
async def get_order(
    order: Order = Depends(order_by_id),
):
    return order


@router.put("/{order_id}/")
async def update_order(
    order_update: OrderUpdate,
    order: Order = Depends(order_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    try:
        return await crud_order.update_order(
            session=session,
            order=order,
            order_update=order_update,
        )
    except SQLAlchemyError:
        handle_database_error()


@router.patch("/{order_id}/")
async def update_order_partial(
    order_update: OrderUpdatePartial,
    order: Order = Depends(order_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    try:
        return await crud_order.update_order(
            session=session,
            order=order,
            order_update=order_update,
            partial=True,
        )
    except SQLAlchemyError:
        handle_database_error()


@router.delete("/{order_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(
    order: Order = Depends(order_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    try:
        await crud_order.delete_order(session=session, order=order)
    except SQLAlchemyError:
        handle_database_error()
