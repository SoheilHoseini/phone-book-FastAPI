# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: phonebook.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fphonebook.proto\"W\n\x07\x43ontact\x12\x0f\n\x02id\x18\x01 \x01(\x0b\x32\x03.ID\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x14\n\x0cphone_number\x18\x04 \x01(\t\"\x10\n\x02ID\x12\n\n\x02id\x18\x01 \x01(\x05\")\n\x0b\x43ontacsList\x12\x1a\n\x08\x63ontacts\x18\x01 \x03(\x0b\x32\x08.Contact\"\x07\n\x05\x45mpty2\x9e\x01\n\tPhoneBook\x12 \n\x06GetAll\x12\x06.Empty\x1a\x0c.ContacsList\"\x00\x12\x16\n\x03Get\x12\x03.ID\x1a\x08.Contact\"\x00\x12\x1e\n\x06\x43reate\x12\x08.Contact\x1a\x08.Contact\"\x00\x12\x1e\n\x06Update\x12\x08.Contact\x1a\x08.Contact\"\x00\x12\x17\n\x06Remove\x12\x03.ID\x1a\x06.Empty\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'phonebook_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_CONTACT']._serialized_start=19
  _globals['_CONTACT']._serialized_end=106
  _globals['_ID']._serialized_start=108
  _globals['_ID']._serialized_end=124
  _globals['_CONTACSLIST']._serialized_start=126
  _globals['_CONTACSLIST']._serialized_end=167
  _globals['_EMPTY']._serialized_start=169
  _globals['_EMPTY']._serialized_end=176
  _globals['_PHONEBOOK']._serialized_start=179
  _globals['_PHONEBOOK']._serialized_end=337
# @@protoc_insertion_point(module_scope)