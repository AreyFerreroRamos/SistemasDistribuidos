# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: daskFunctions.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x64\x61skFunctions.proto\"\x1d\n\x08NameFile\x12\x11\n\tname_file\x18\x01 \x01(\t\")\n\x05\x46ield\x12\x11\n\tname_file\x18\x01 \x01(\t\x12\r\n\x05\x66ield\x18\x02 \x01(\t\"\x1b\n\nFileReturn\x12\r\n\x05value\x18\x01 \x01(\t\"\x1c\n\x0bValueReturn\x12\r\n\x05value\x18\x01 \x01(\x02\x32r\n\rDaskFunctions\x12#\n\x07ReadCSV\x12\t.NameFile\x1a\x0b.FileReturn\"\x00\x12\x1d\n\x03Max\x12\x06.Field\x1a\x0c.ValueReturn\"\x00\x12\x1d\n\x03Min\x12\x06.Field\x1a\x0c.ValueReturn\"\x00\x62\x06proto3')



_NAMEFILE = DESCRIPTOR.message_types_by_name['NameFile']
_FIELD = DESCRIPTOR.message_types_by_name['Field']
_FILERETURN = DESCRIPTOR.message_types_by_name['FileReturn']
_VALUERETURN = DESCRIPTOR.message_types_by_name['ValueReturn']
NameFile = _reflection.GeneratedProtocolMessageType('NameFile', (_message.Message,), {
  'DESCRIPTOR' : _NAMEFILE,
  '__module__' : 'daskFunctions_pb2'
  # @@protoc_insertion_point(class_scope:NameFile)
  })
_sym_db.RegisterMessage(NameFile)

Field = _reflection.GeneratedProtocolMessageType('Field', (_message.Message,), {
  'DESCRIPTOR' : _FIELD,
  '__module__' : 'daskFunctions_pb2'
  # @@protoc_insertion_point(class_scope:Field)
  })
_sym_db.RegisterMessage(Field)

FileReturn = _reflection.GeneratedProtocolMessageType('FileReturn', (_message.Message,), {
  'DESCRIPTOR' : _FILERETURN,
  '__module__' : 'daskFunctions_pb2'
  # @@protoc_insertion_point(class_scope:FileReturn)
  })
_sym_db.RegisterMessage(FileReturn)

ValueReturn = _reflection.GeneratedProtocolMessageType('ValueReturn', (_message.Message,), {
  'DESCRIPTOR' : _VALUERETURN,
  '__module__' : 'daskFunctions_pb2'
  # @@protoc_insertion_point(class_scope:ValueReturn)
  })
_sym_db.RegisterMessage(ValueReturn)

_DASKFUNCTIONS = DESCRIPTOR.services_by_name['DaskFunctions']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NAMEFILE._serialized_start=23
  _NAMEFILE._serialized_end=52
  _FIELD._serialized_start=54
  _FIELD._serialized_end=95
  _FILERETURN._serialized_start=97
  _FILERETURN._serialized_end=124
  _VALUERETURN._serialized_start=126
  _VALUERETURN._serialized_end=154
  _DASKFUNCTIONS._serialized_start=156
  _DASKFUNCTIONS._serialized_end=270
# @@protoc_insertion_point(module_scope)
