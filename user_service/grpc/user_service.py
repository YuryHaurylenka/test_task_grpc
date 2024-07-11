import asyncio
import logging

import grpc
from sqlalchemy.ext.asyncio import AsyncSession

import user_pb2 as pb2
import user_pb2_grpc as pb2_grpc
from user_service.app.crud.user import get_user


class UserServicer(pb2_grpc.UserServiceServicer):
    async def GetUserResponse(
        self,
        request: pb2.UserRequest,
        context: grpc.aio.ServicerContext,
    ) -> pb2.GetUserResponse:
        user_id = request.user_id
        async with AsyncSession() as session:
            user = await get_user(session, user_id)
            if user:
                return pb2.GetUserResponse(
                    user_id=user.user_id,
                    username=user.username,
                    email=user.email,
                    age=user.age,
                )
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details(f"User with id {user_id} not found")
                return pb2.GetUserResponse()


async def serve() -> None:
    server = grpc.aio.server()
    pb2_grpc.add_UserServiceServicer_to_server(UserServicer(), server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    print("Server started. Listening on port 50051.")
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("User Server Starter...")
    asyncio.run(serve())
