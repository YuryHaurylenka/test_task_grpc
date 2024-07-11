import asyncio
import logging

import grpc
from sqlalchemy.ext.asyncio import AsyncSession

import order_pb2 as pb2
import order_pb2_grpc as pb2_grpc
from order_service.app.crud.order import create_order

from order_service.app.schemas import OrderCreate


class OrderServicer(pb2_grpc.OrderServiceServicer):
    async def CreateOrder(
        self,
        request: pb2.CreateOrderRequest,
        context: grpc.aio.ServicerContext,
    ) -> pb2.CreateOrderResponse:
        user_id = request.user_id
        order_name = request.order_name
        description = request.description
        try:
            async with grpc.aio.insecure_channel("localhost:50051") as channel:
                stub = pb2_grpc.UserExistenceCheckStub(channel)
                user_exists_request = pb2_grpc.CheckUserExistenceRequest(
                    user_id=user_id
                )
                await stub.CheckUserExistence(user_exists_request)
        except grpc.aio.AioRpcError as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"User with id {user_id} not found")
            return pb2.CreateOrderResponse(
                message=f"Failed to create order for user_id: {user_id}"
            )

        async with AsyncSession() as session:
            try:
                order_in = OrderCreate(
                    user_id=user_id, order_name=order_name, description=description
                )
                order = await create_order(session, order_in)
                return pb2.CreateOrderResponse(
                    message=f"Order created successfully for user_id: {user_id}"
                )
            except Exception as e:
                logging.error(f"Error creating order: {e}")
                context.set_code(grpc.StatusCode.INTERNAL)
                context.set_details(f"Failed to create order for user_id: {user_id}")
                return pb2.CreateOrderResponse(
                    message=f"Failed to create order for user_id: {user_id}"
                )


async def serve() -> None:
    server = grpc.aio.server()
    pb2_grpc.add_OrderServiceServicer_to_server(OrderServicer(), server)
    listen_addr = "[::]:50052"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    print("Order Service started. Listening on port 50052.")
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Order Service Starter...")
    asyncio.run(serve())
