# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ecommerce.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ecommerce.proto',
  package='ecommerce',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0f\x65\x63ommerce.proto\x12\tecommerce\"=\n\x08\x43ustomer\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\"\x82\x01\n\x07Product\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04slug\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x16\n\x0eprice_in_cents\x18\x04 \x01(\x05\x12\x30\n\x0e\x64iscount_value\x18\x05 \x01(\x0b\x32\x18.ecommerce.DiscountValue\"4\n\rDiscountValue\x12\x0b\n\x03pct\x18\x01 \x01(\x02\x12\x16\n\x0evalue_in_cents\x18\x02 \x01(\x05\"]\n\x0f\x44iscountRequest\x12%\n\x08\x63ustomer\x18\x01 \x01(\x0b\x32\x13.ecommerce.Customer\x12#\n\x07product\x18\x02 \x01(\x0b\x32\x12.ecommerce.Product\"7\n\x10\x44iscountResponse\x12#\n\x07product\x18\x01 \x01(\x0b\x32\x12.ecommerce.Product2V\n\x08\x44iscount\x12J\n\rApplyDiscount\x12\x1a.ecommerce.DiscountRequest\x1a\x1b.ecommerce.DiscountResponse\"\x00\x62\x06proto3')
)




_CUSTOMER = _descriptor.Descriptor(
  name='Customer',
  full_name='ecommerce.Customer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ecommerce.Customer.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='ecommerce.Customer.first_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='ecommerce.Customer.last_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=30,
  serialized_end=91,
)


_PRODUCT = _descriptor.Descriptor(
  name='Product',
  full_name='ecommerce.Product',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ecommerce.Product.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slug', full_name='ecommerce.Product.slug', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='ecommerce.Product.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price_in_cents', full_name='ecommerce.Product.price_in_cents', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='discount_value', full_name='ecommerce.Product.discount_value', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=94,
  serialized_end=224,
)


_DISCOUNTVALUE = _descriptor.Descriptor(
  name='DiscountValue',
  full_name='ecommerce.DiscountValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pct', full_name='ecommerce.DiscountValue.pct', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value_in_cents', full_name='ecommerce.DiscountValue.value_in_cents', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=226,
  serialized_end=278,
)


_DISCOUNTREQUEST = _descriptor.Descriptor(
  name='DiscountRequest',
  full_name='ecommerce.DiscountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer', full_name='ecommerce.DiscountRequest.customer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='product', full_name='ecommerce.DiscountRequest.product', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=280,
  serialized_end=373,
)


_DISCOUNTRESPONSE = _descriptor.Descriptor(
  name='DiscountResponse',
  full_name='ecommerce.DiscountResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='product', full_name='ecommerce.DiscountResponse.product', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=375,
  serialized_end=430,
)

_PRODUCT.fields_by_name['discount_value'].message_type = _DISCOUNTVALUE
_DISCOUNTREQUEST.fields_by_name['customer'].message_type = _CUSTOMER
_DISCOUNTREQUEST.fields_by_name['product'].message_type = _PRODUCT
_DISCOUNTRESPONSE.fields_by_name['product'].message_type = _PRODUCT
DESCRIPTOR.message_types_by_name['Customer'] = _CUSTOMER
DESCRIPTOR.message_types_by_name['Product'] = _PRODUCT
DESCRIPTOR.message_types_by_name['DiscountValue'] = _DISCOUNTVALUE
DESCRIPTOR.message_types_by_name['DiscountRequest'] = _DISCOUNTREQUEST
DESCRIPTOR.message_types_by_name['DiscountResponse'] = _DISCOUNTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Customer = _reflection.GeneratedProtocolMessageType('Customer', (_message.Message,), dict(
  DESCRIPTOR = _CUSTOMER,
  __module__ = 'ecommerce_pb2'
  # @@protoc_insertion_point(class_scope:ecommerce.Customer)
  ))
_sym_db.RegisterMessage(Customer)

Product = _reflection.GeneratedProtocolMessageType('Product', (_message.Message,), dict(
  DESCRIPTOR = _PRODUCT,
  __module__ = 'ecommerce_pb2'
  # @@protoc_insertion_point(class_scope:ecommerce.Product)
  ))
_sym_db.RegisterMessage(Product)

DiscountValue = _reflection.GeneratedProtocolMessageType('DiscountValue', (_message.Message,), dict(
  DESCRIPTOR = _DISCOUNTVALUE,
  __module__ = 'ecommerce_pb2'
  # @@protoc_insertion_point(class_scope:ecommerce.DiscountValue)
  ))
_sym_db.RegisterMessage(DiscountValue)

DiscountRequest = _reflection.GeneratedProtocolMessageType('DiscountRequest', (_message.Message,), dict(
  DESCRIPTOR = _DISCOUNTREQUEST,
  __module__ = 'ecommerce_pb2'
  # @@protoc_insertion_point(class_scope:ecommerce.DiscountRequest)
  ))
_sym_db.RegisterMessage(DiscountRequest)

DiscountResponse = _reflection.GeneratedProtocolMessageType('DiscountResponse', (_message.Message,), dict(
  DESCRIPTOR = _DISCOUNTRESPONSE,
  __module__ = 'ecommerce_pb2'
  # @@protoc_insertion_point(class_scope:ecommerce.DiscountResponse)
  ))
_sym_db.RegisterMessage(DiscountResponse)



_DISCOUNT = _descriptor.ServiceDescriptor(
  name='Discount',
  full_name='ecommerce.Discount',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=432,
  serialized_end=518,
  methods=[
  _descriptor.MethodDescriptor(
    name='ApplyDiscount',
    full_name='ecommerce.Discount.ApplyDiscount',
    index=0,
    containing_service=None,
    input_type=_DISCOUNTREQUEST,
    output_type=_DISCOUNTRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DISCOUNT)

DESCRIPTOR.services_by_name['Discount'] = _DISCOUNT

# @@protoc_insertion_point(module_scope)
