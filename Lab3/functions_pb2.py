# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: functions.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x66unctions.proto\"\x18\n\x06Insult\x12\x0e\n\x06insult\x18\x01 \x01(\t\"\x07\n\x05\x45mpty2l\n\tFunctions\x12\x1f\n\tAddInsult\x12\x07.Insult\x1a\x07.Insult\"\x00\x12\x1f\n\nGetInsults\x12\x06.Empty\x1a\x07.Insult\"\x00\x12\x1d\n\x08Insultme\x12\x06.Empty\x1a\x07.Insult\"\x00\x62\x06proto3')



_INSULT = DESCRIPTOR.message_types_by_name['Insult']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
Insult = _reflection.GeneratedProtocolMessageType('Insult', (_message.Message,), {
  'DESCRIPTOR' : _INSULT,
  '__module__' : 'functions_pb2'
  # @@protoc_insertion_point(class_scope:Insult)
  })
_sym_db.RegisterMessage(Insult)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'functions_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

_FUNCTIONS = DESCRIPTOR.services_by_name['Functions']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INSULT._serialized_start=19
  _INSULT._serialized_end=43
  _EMPTY._serialized_start=45
  _EMPTY._serialized_end=52
  _FUNCTIONS._serialized_start=54
  _FUNCTIONS._serialized_end=162
# @@protoc_insertion_point(module_scope)
