from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Contact(_message.Message):
    __slots__ = ["id", "first_name", "last_name", "phone_number"]
    ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    id: ID
    first_name: str
    last_name: str
    phone_number: str
    def __init__(self, id: _Optional[_Union[ID, _Mapping]] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., phone_number: _Optional[str] = ...) -> None: ...

class ID(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ContacsList(_message.Message):
    __slots__ = ["contacts"]
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    contacts: _containers.RepeatedCompositeFieldContainer[Contact]
    def __init__(self, contacts: _Optional[_Iterable[_Union[Contact, _Mapping]]] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
