# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qa_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10qa_service.proto\x12\nqa_service\"O\n\x0fQuestionRequest\x12\x10\n\x08question\x18\x01 \x01(\t\x12\x16\n\x0e\x63ontext_tables\x18\x02 \x03(\t\x12\x12\n\nsession_id\x18\x03 \x01(\t\"T\n\x0e\x41nswerResponse\x12\x0e\n\x06\x61nswer\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x12\n\nconfidence\x18\x04 \x01(\x02\"\x16\n\x14\x43reateSessionRequest\"K\n\x15\x43reateSessionResponse\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\r\n\x05\x65rror\x18\x03 \x01(\t\"*\n\x14\x44\x65leteSessionRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\"7\n\x15\x44\x65leteSessionResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t2\x8c\x02\n\x10QuestionAnswerer\x12H\n\x0b\x41skQuestion\x12\x1b.qa_service.QuestionRequest\x1a\x1a.qa_service.AnswerResponse\"\x00\x12V\n\rCreateSession\x12 .qa_service.CreateSessionRequest\x1a!.qa_service.CreateSessionResponse\"\x00\x12V\n\rDeleteSession\x12 .qa_service.DeleteSessionRequest\x1a!.qa_service.DeleteSessionResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'qa_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_QUESTIONREQUEST']._serialized_start=32
  _globals['_QUESTIONREQUEST']._serialized_end=111
  _globals['_ANSWERRESPONSE']._serialized_start=113
  _globals['_ANSWERRESPONSE']._serialized_end=197
  _globals['_CREATESESSIONREQUEST']._serialized_start=199
  _globals['_CREATESESSIONREQUEST']._serialized_end=221
  _globals['_CREATESESSIONRESPONSE']._serialized_start=223
  _globals['_CREATESESSIONRESPONSE']._serialized_end=298
  _globals['_DELETESESSIONREQUEST']._serialized_start=300
  _globals['_DELETESESSIONREQUEST']._serialized_end=342
  _globals['_DELETESESSIONRESPONSE']._serialized_start=344
  _globals['_DELETESESSIONRESPONSE']._serialized_end=399
  _globals['_QUESTIONANSWERER']._serialized_start=402
  _globals['_QUESTIONANSWERER']._serialized_end=670
# @@protoc_insertion_point(module_scope)
