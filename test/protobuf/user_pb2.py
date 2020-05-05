# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/user.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobuf/user.proto',
  package='proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13protobuf/user.proto\x12\x05proto\"<\n\x14QueryUserListRequest\x12\x12\n\nstarted_at\x18\x01 \x01(\x04\x12\x10\n\x08\x65nded_at\x18\x02 \x01(\x04\"\x1b\n\rDetailRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"&\n\x08UserList\x12\x1a\n\x05users\x18\x01 \x03(\x0b\x32\x0b.proto.User\"$\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08username\x18\x02 \x01(\t2}\n\x0bUserService\x12\x32\n\x0bGetUserById\x12\x14.proto.DetailRequest\x1a\x0b.proto.User\"\x00\x12:\n\x08GetUsers\x12\x1b.proto.QueryUserListRequest\x1a\x0f.proto.UserList\"\x00\x62\x06proto3')
)




_QUERYUSERLISTREQUEST = _descriptor.Descriptor(
  name='QueryUserListRequest',
  full_name='proto.QueryUserListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='started_at', full_name='proto.QueryUserListRequest.started_at', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ended_at', full_name='proto.QueryUserListRequest.ended_at', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=90,
)


_DETAILREQUEST = _descriptor.Descriptor(
  name='DetailRequest',
  full_name='proto.DetailRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='proto.DetailRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=119,
)


_USERLIST = _descriptor.Descriptor(
  name='UserList',
  full_name='proto.UserList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='users', full_name='proto.UserList.users', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=159,
)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='proto.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='proto.User.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='proto.User.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=161,
  serialized_end=197,
)

_USERLIST.fields_by_name['users'].message_type = _USER
DESCRIPTOR.message_types_by_name['QueryUserListRequest'] = _QUERYUSERLISTREQUEST
DESCRIPTOR.message_types_by_name['DetailRequest'] = _DETAILREQUEST
DESCRIPTOR.message_types_by_name['UserList'] = _USERLIST
DESCRIPTOR.message_types_by_name['User'] = _USER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryUserListRequest = _reflection.GeneratedProtocolMessageType('QueryUserListRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYUSERLISTREQUEST,
  __module__ = 'protobuf.user_pb2'
  # @@protoc_insertion_point(class_scope:proto.QueryUserListRequest)
  ))
_sym_db.RegisterMessage(QueryUserListRequest)

DetailRequest = _reflection.GeneratedProtocolMessageType('DetailRequest', (_message.Message,), dict(
  DESCRIPTOR = _DETAILREQUEST,
  __module__ = 'protobuf.user_pb2'
  # @@protoc_insertion_point(class_scope:proto.DetailRequest)
  ))
_sym_db.RegisterMessage(DetailRequest)

UserList = _reflection.GeneratedProtocolMessageType('UserList', (_message.Message,), dict(
  DESCRIPTOR = _USERLIST,
  __module__ = 'protobuf.user_pb2'
  # @@protoc_insertion_point(class_scope:proto.UserList)
  ))
_sym_db.RegisterMessage(UserList)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), dict(
  DESCRIPTOR = _USER,
  __module__ = 'protobuf.user_pb2'
  # @@protoc_insertion_point(class_scope:proto.User)
  ))
_sym_db.RegisterMessage(User)



_USERSERVICE = _descriptor.ServiceDescriptor(
  name='UserService',
  full_name='proto.UserService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=199,
  serialized_end=324,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetUserById',
    full_name='proto.UserService.GetUserById',
    index=0,
    containing_service=None,
    input_type=_DETAILREQUEST,
    output_type=_USER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetUsers',
    full_name='proto.UserService.GetUsers',
    index=1,
    containing_service=None,
    input_type=_QUERYUSERLISTREQUEST,
    output_type=_USERLIST,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERSERVICE)

DESCRIPTOR.services_by_name['UserService'] = _USERSERVICE

# @@protoc_insertion_point(module_scope)
