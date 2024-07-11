from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from order_service.app.core import db_helper
from order_service.app.crud import order as crud_order
from order_service.app.dependencies import order_by_id
from order_service.app.schemas import (
    Order,
    OrderCreate,
    OrderUpdate,
    OrderUpdatePartial,
)

router = APIRouter(tags=["Order"])


@router.get("/", response_model=list[Order])
async def get_orders(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud_order.get_orders(session=session)


@router.post(
    "/",
    response_model=Order,
    status_code=status.HTTP_201_CREATED,
)
async def create_order(
    order_in: OrderCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud_order.create_order(session=session, order_in=order_in)


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
    return await crud_order.update_order(
        session=session,
        order=order,
        order_update=order_update,
    )


@router.patch("/{order_id}/")
async def update_order_partial(
    order_update: OrderUpdatePartial,
    order: Order = Depends(order_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud_order.update_order(
        session=session,
        order=order,
        order_update=order_update,
        partial=True,
    )


@router.delete("/{order_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(
    order: Order = Depends(order_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud_order.delete_order(session=session, order=order)
