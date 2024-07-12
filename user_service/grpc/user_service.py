import logging
from concurrent import futures

import grpc

from user_service.app.core import db_helper
from user_service.app.models import User
from user_service.grpc import user_pb2 as pb2, user_pb2_grpc as pb2_grpc


class UserServiceServicer(pb2_grpc.UserServiceServicer):
    async def GetUser(self, request, context):
        session = db_helper.get_scoped_session()
        async with session() as s:
            user = await s.get(User, request.user_id)
            if user is None:
                context.set_details(f"User with id {request.user_id} not found")
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return pb2.UserResponse()
            return pb2.UserResponse(
                user_id=str(user.user_id),
                username=user.username,
                email=user.email,
                age=user.age,
            )


async def serve_grpc():
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_UserServiceServicer_to_server(UserServiceServicer(), server)
    server.add_insecure_port("0.0.0.0:50051")
    logging.info("Starting gRPC server on port 50051...")
    await server.start()
    await server.wait_for_termination()
