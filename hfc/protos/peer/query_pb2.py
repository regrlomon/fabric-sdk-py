# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hfc/protos/peer/query.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hfc/protos/peer/query.proto',
  package='hfc.protos.peer',
  syntax='proto3',
  serialized_pb=_b('\n\x1bhfc/protos/peer/query.proto\x12\x0fhfc.protos.peer\"L\n\x16\x43haincodeQueryResponse\x12\x32\n\nchaincodes\x18\x01 \x03(\x0b\x32\x1e.hfc.protos.peer.ChaincodeInfo\"g\n\rChaincodeInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\r\n\x05input\x18\x04 \x01(\t\x12\x0c\n\x04\x65scc\x18\x05 \x01(\t\x12\x0c\n\x04vscc\x18\x06 \x01(\t\"F\n\x14\x43hannelQueryResponse\x12.\n\x08\x63hannels\x18\x01 \x03(\x0b\x32\x1c.hfc.protos.peer.ChannelInfo\"!\n\x0b\x43hannelInfo\x12\x12\n\nchannel_id\x18\x01 \x01(\tB+Z)github.com/hyperledger/fabric/protos/peerb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CHAINCODEQUERYRESPONSE = _descriptor.Descriptor(
  name='ChaincodeQueryResponse',
  full_name='hfc.protos.peer.ChaincodeQueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chaincodes', full_name='hfc.protos.peer.ChaincodeQueryResponse.chaincodes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=124,
)


_CHAINCODEINFO = _descriptor.Descriptor(
  name='ChaincodeInfo',
  full_name='hfc.protos.peer.ChaincodeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='hfc.protos.peer.ChaincodeInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='hfc.protos.peer.ChaincodeInfo.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path', full_name='hfc.protos.peer.ChaincodeInfo.path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='input', full_name='hfc.protos.peer.ChaincodeInfo.input', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='escc', full_name='hfc.protos.peer.ChaincodeInfo.escc', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vscc', full_name='hfc.protos.peer.ChaincodeInfo.vscc', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=229,
)


_CHANNELQUERYRESPONSE = _descriptor.Descriptor(
  name='ChannelQueryResponse',
  full_name='hfc.protos.peer.ChannelQueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channels', full_name='hfc.protos.peer.ChannelQueryResponse.channels', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=231,
  serialized_end=301,
)


_CHANNELINFO = _descriptor.Descriptor(
  name='ChannelInfo',
  full_name='hfc.protos.peer.ChannelInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='hfc.protos.peer.ChannelInfo.channel_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=303,
  serialized_end=336,
)

_CHAINCODEQUERYRESPONSE.fields_by_name['chaincodes'].message_type = _CHAINCODEINFO
_CHANNELQUERYRESPONSE.fields_by_name['channels'].message_type = _CHANNELINFO
DESCRIPTOR.message_types_by_name['ChaincodeQueryResponse'] = _CHAINCODEQUERYRESPONSE
DESCRIPTOR.message_types_by_name['ChaincodeInfo'] = _CHAINCODEINFO
DESCRIPTOR.message_types_by_name['ChannelQueryResponse'] = _CHANNELQUERYRESPONSE
DESCRIPTOR.message_types_by_name['ChannelInfo'] = _CHANNELINFO

ChaincodeQueryResponse = _reflection.GeneratedProtocolMessageType('ChaincodeQueryResponse', (_message.Message,), dict(
  DESCRIPTOR = _CHAINCODEQUERYRESPONSE,
  __module__ = 'hfc.protos.peer.query_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.peer.ChaincodeQueryResponse)
  ))
_sym_db.RegisterMessage(ChaincodeQueryResponse)

ChaincodeInfo = _reflection.GeneratedProtocolMessageType('ChaincodeInfo', (_message.Message,), dict(
  DESCRIPTOR = _CHAINCODEINFO,
  __module__ = 'hfc.protos.peer.query_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.peer.ChaincodeInfo)
  ))
_sym_db.RegisterMessage(ChaincodeInfo)

ChannelQueryResponse = _reflection.GeneratedProtocolMessageType('ChannelQueryResponse', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELQUERYRESPONSE,
  __module__ = 'hfc.protos.peer.query_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.peer.ChannelQueryResponse)
  ))
_sym_db.RegisterMessage(ChannelQueryResponse)

ChannelInfo = _reflection.GeneratedProtocolMessageType('ChannelInfo', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELINFO,
  __module__ = 'hfc.protos.peer.query_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.peer.ChannelInfo)
  ))
_sym_db.RegisterMessage(ChannelInfo)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z)github.com/hyperledger/fabric/protos/peer'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)