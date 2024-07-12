import asyncio
import uuid

import grpc

from user_service.grpc import user_pb2, user_pb2_grpc

# TODO: из-за импорта докер не запускается


async def check_user_exists(user_id: uuid.UUID) -> bool:
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = user_pb2_grpc.UserServiceStub(channel)
        request = user_pb2.UserRequest(user_id=str(user_id))
        response = await stub.GetUser(request)
        return response.user_id == str(user_id)
