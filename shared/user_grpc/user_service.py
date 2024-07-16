import asyncio
import logging
from concurrent import futures

import grpc

from shared.user_grpc import user_pb2 as pb2, user_pb2_grpc as pb2_grpc
from user_service.app.core import db_helper
from user_service.app.models import User

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logging.getLogger("grpc").setLevel(logging.ERROR)


class UserServiceServicer(pb2_grpc.UserServiceServicer):
    async def GetUser(self, request, context):
        logging.info(f"Received GetUser request for user_id: {request.user_id}")
        try:
            session = db_helper.get_scoped_session()
            async with session() as s:
                user = await s.get(User, request.user_id)
                if user is None:
                    context.set_details(f"User with id {request.user_id} not found")
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    logging.error(f"User with id {request.user_id} not found")
                    return pb2.UserResponse()
                logging.info(
                    f"User with id {request.user_id} found: Username = {user.username}, email = {user.email}, age = {user.age}"
                )
                return pb2.UserResponse(
                    user_id=str(user.user_id),
                    username=user.username,
                    email=user.email,
                    age=user.age,
                )
        except grpc.aio.AioRpcError as e:
            logging.error(f"Error while checking user existence: {e.details()}")
            context.set_details(f"Error while checking user existence: {e.details()}")
            context.set_code(grpc.StatusCode.INTERNAL)


async def serve_grpc():
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_UserServiceServicer_to_server(UserServiceServicer(), server)
    server.add_insecure_port("0.0.0.0:50051")
    logging.info("Starting gRPC server on port 50051...")
    try:
        await server.start()
        await server.wait_for_termination()
    except asyncio.CancelledError:
        logging.info("gRPC server shutdown requested.")
        await server.stop(None)
