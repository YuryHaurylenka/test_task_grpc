# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc/user.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fgrpc/user.proto\x12\x04user\"!\n\x0eGetUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"P\n\x0fGetUserResponse\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x0b\n\x03\x61ge\x18\x04 \x01(\x05\x32\x45\n\x0bUserService\x12\x36\n\x07GetUser\x12\x14.user.GetUserRequest\x1a\x15.user.GetUserResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpc.user_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GETUSERREQUEST']._serialized_start=25
  _globals['_GETUSERREQUEST']._serialized_end=58
  _globals['_GETUSERRESPONSE']._serialized_start=60
  _globals['_GETUSERRESPONSE']._serialized_end=140
  _globals['_USERSERVICE']._serialized_start=142
  _globals['_USERSERVICE']._serialized_end=211
# @@protoc_insertion_point(module_scope)
