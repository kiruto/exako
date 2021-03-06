# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rest_request.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rest_request.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x12rest_request.proto\x1a\x19google/protobuf/any.proto\"\x9b\x02\n\x07Request\x12\x1f\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\x0f.Request.Action\x12\x0e\n\x06target\x18\x02 \x03(\t\x12\x0e\n\x06source\x18\x03 \x01(\t\x12\x16\n\x07require\x18\x04 \x03(\x0b\x32\x05.Dict\x12\x13\n\x04sort\x18\x05 \x03(\x0b\x32\x05.Sort\x12\r\n\x05limit\x18\x06 \x01(\x05\x12\x0e\n\x06offset\x18\x07 \x01(\x03\x12\"\n\x04\x61rgs\x18\x08 \x01(\x0b\x32\x14.google.protobuf.Any\x12%\n\x07\x63ontent\x18\t \x03(\x0b\x32\x14.google.protobuf.Any\"8\n\x06\x41\x63tion\x12\n\n\x06SELECT\x10\x00\x12\n\n\x06INSERT\x10\x01\x12\n\n\x06UPDATE\x10\x02\x12\n\n\x06\x44\x45LETE\x10\x03\"r\n\x08Response\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12$\n\x06result\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any\x12%\n\x07\x63ontent\x18\x03 \x03(\x0b\x32\x14.google.protobuf.Any\"e\n\x04\x44ict\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x1e\n\x07\x63ompare\x18\x03 \x01(\x0e\x32\r.Dict.Compare\"!\n\x07\x43ompare\x12\x06\n\x02LT\x10\x00\x12\x06\n\x02\x45Q\x10\x01\x12\x06\n\x02GT\x10\x02\"T\n\x04Sort\x12\x0e\n\x06\x63olumn\x18\x01 \x01(\t\x12\x1e\n\x07orderBy\x18\x02 \x01(\x0e\x32\r.Sort.OrderBy\"\x1c\n\x07OrderBy\x12\x07\n\x03\x41SC\x10\x00\x12\x08\n\x04\x44\x45SC\x10\x01\"6\n\x03\x41rg\x12\x0c\n\x04text\x18\x01 \x03(\t\x12!\n\x03obj\x18\x02 \x03(\x0b\x32\x14.google.protobuf.Anyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_REQUEST_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='Request.Action',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SELECT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INSERT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=277,
  serialized_end=333,
)
_sym_db.RegisterEnumDescriptor(_REQUEST_ACTION)

_DICT_COMPARE = _descriptor.EnumDescriptor(
  name='Compare',
  full_name='Dict.Compare',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EQ', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GT', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=519,
  serialized_end=552,
)
_sym_db.RegisterEnumDescriptor(_DICT_COMPARE)

_SORT_ORDERBY = _descriptor.EnumDescriptor(
  name='OrderBy',
  full_name='Sort.OrderBy',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ASC', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DESC', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=610,
  serialized_end=638,
)
_sym_db.RegisterEnumDescriptor(_SORT_ORDERBY)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='Request.action', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target', full_name='Request.target', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='Request.source', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='require', full_name='Request.require', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort', full_name='Request.sort', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='limit', full_name='Request.limit', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offset', full_name='Request.offset', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='args', full_name='Request.args', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='Request.content', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REQUEST_ACTION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=333,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='Response.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg', full_name='Response.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='Response.result', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='Response.content', index=3,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=335,
  serialized_end=449,
)


_DICT = _descriptor.Descriptor(
  name='Dict',
  full_name='Dict',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Dict.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='Dict.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='compare', full_name='Dict.compare', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DICT_COMPARE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=451,
  serialized_end=552,
)


_SORT = _descriptor.Descriptor(
  name='Sort',
  full_name='Sort',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='column', full_name='Sort.column', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orderBy', full_name='Sort.orderBy', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SORT_ORDERBY,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=554,
  serialized_end=638,
)


_ARG = _descriptor.Descriptor(
  name='Arg',
  full_name='Arg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='Arg.text', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='obj', full_name='Arg.obj', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=640,
  serialized_end=694,
)

_REQUEST.fields_by_name['action'].enum_type = _REQUEST_ACTION
_REQUEST.fields_by_name['require'].message_type = _DICT
_REQUEST.fields_by_name['sort'].message_type = _SORT
_REQUEST.fields_by_name['args'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_REQUEST.fields_by_name['content'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_REQUEST_ACTION.containing_type = _REQUEST
_RESPONSE.fields_by_name['result'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_RESPONSE.fields_by_name['content'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_DICT.fields_by_name['compare'].enum_type = _DICT_COMPARE
_DICT_COMPARE.containing_type = _DICT
_SORT.fields_by_name['orderBy'].enum_type = _SORT_ORDERBY
_SORT_ORDERBY.containing_type = _SORT
_ARG.fields_by_name['obj'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['Dict'] = _DICT
DESCRIPTOR.message_types_by_name['Sort'] = _SORT
DESCRIPTOR.message_types_by_name['Arg'] = _ARG

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'rest_request_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'rest_request_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  ))
_sym_db.RegisterMessage(Response)

Dict = _reflection.GeneratedProtocolMessageType('Dict', (_message.Message,), dict(
  DESCRIPTOR = _DICT,
  __module__ = 'rest_request_pb2'
  # @@protoc_insertion_point(class_scope:Dict)
  ))
_sym_db.RegisterMessage(Dict)

Sort = _reflection.GeneratedProtocolMessageType('Sort', (_message.Message,), dict(
  DESCRIPTOR = _SORT,
  __module__ = 'rest_request_pb2'
  # @@protoc_insertion_point(class_scope:Sort)
  ))
_sym_db.RegisterMessage(Sort)

Arg = _reflection.GeneratedProtocolMessageType('Arg', (_message.Message,), dict(
  DESCRIPTOR = _ARG,
  __module__ = 'rest_request_pb2'
  # @@protoc_insertion_point(class_scope:Arg)
  ))
_sym_db.RegisterMessage(Arg)


# @@protoc_insertion_point(module_scope)
