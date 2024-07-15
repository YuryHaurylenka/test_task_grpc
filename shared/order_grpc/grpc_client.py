import uuid

import grpc

from shared.user_grpc import user_pb2, user_pb2_grpc


async def check_user_exists(user_id: uuid.UUID) -> bool:
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = user_pb2_grpc.UserServiceStub(channel)
        request = user_pb2.UserRequest(user_id=str(user_id))
        try:
            response = await stub.GetUser(request)
            return response.user_id == str(user_id)
        except grpc.aio.AioRpcError as e:
            print(f"Error while checking user existence: {e}")
            return False
