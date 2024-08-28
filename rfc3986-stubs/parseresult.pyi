from typing import AnyStr, Generic
from rfc3986 import uri
from typing import Self

__all__ = ["ParseResult", "ParseResultBytes"]

class ParseResultMixin(Generic[AnyStr]):
    userinfo: AnyStr | None
    host: AnyStr | None
    port: int | None
    query: AnyStr | None
    encoding: str
    @property
    def authority(self) -> AnyStr | None: ...
    def geturl(self) -> AnyStr: ...
    @property
    def hostname(self) -> AnyStr | None: ...
    @property
    def netloc(self) -> AnyStr | None: ...
    @property
    def params(self) -> AnyStr | None: ...

class ParseResult(ParseResultMixin[str]):
    scheme: str | None
    userinfo: str | None
    host: str | None
    port: int | None
    path: str | None
    query: str | None
    fragment: str | None
    encoding: str
    reference: uri.URIReference
    def __new__(
        cls,
        scheme: str | None,
        userinfo: str | None,
        host: str | None,
        port: int | None,
        path: str | None,
        query: str | None,
        fragment: str | None,
        uri_ref: uri.URIReference,
        encoding: str = ...,
    ) -> Self: ...
    @classmethod
    def from_parts(
        cls,
        scheme: str | None = None,
        userinfo: str | None = None,
        host: str | None = None,
        port: int | str | None = None,
        path: str | None = None,
        query: str | None = None,
        fragment: str | None = None,
        encoding: str = ...,
    ) -> Self: ...
    @classmethod
    def from_string(
        cls,
        uri_string: str | bytes,
        encoding: str = ...,
        strict: bool = True,
        lazy_normalize: bool = True,
    ) -> Self: ...
    @property
    def authority(self) -> str | None: ...
    def copy_with(
        self,
        scheme: str | None = ...,
        userinfo: str | None = ...,
        host: str | None = ...,
        port: int | str | None = ...,
        path: str | None = ...,
        query: str | None = ...,
        fragment: str | None = ...,
    ) -> ParseResult: ...
    def encode(self, encoding: str | None = None) -> ParseResultBytes: ...
    def unsplit(self, use_idna: bool = ...) -> str: ...

class ParseResultBytes(ParseResultMixin[bytes]):
    scheme: bytes | None
    userinfo: bytes | None
    host: bytes | None
    port: int | None
    path: bytes | None
    query: bytes | None
    fragment: bytes | None
    encoding: str
    reference: uri.URIReference
    lazy_normalize: bool
    def __new__(
        cls,
        scheme: bytes | None,
        userinfo: bytes | None,
        host: bytes | None,
        port: int | None,
        path: bytes | None,
        query: bytes | None,
        fragment: bytes | None,
        uri_ref: uri.URIReference,
        encoding: str = ...,
        lazy_normalize: bool = True,
    ) -> Self: ...
    @classmethod
    def from_parts(
        cls,
        scheme: str | None = None,
        userinfo: str | None = None,
        host: str | None = None,
        port: int | str | None = None,
        path: str | None = None,
        query: str | None = None,
        fragment: str | None = None,
        encoding: str = ...,
        lazy_normalize: bool = True,
    ) -> Self: ...
    @classmethod
    def from_string(
        cls,
        uri_string: str | bytes,
        encoding: str = ...,
        strict: bool = True,
        lazy_normalize: bool = True,
    ) -> Self: ...
    @property
    def authority(self) -> bytes: ...
    def copy_with(
        self,
        scheme: str | bytes | None = ...,
        userinfo: str | bytes | None = ...,
        host: str | bytes | None = ...,
        port: int | str | bytes | None = ...,
        path: str | bytes | None = ...,
        query: str | bytes | None = ...,
        fragment: str | bytes | None = ...,
        lazy_normalize: bool = True,
    ) -> ParseResultBytes: ...
    def unsplit(self, use_idna: bool = ...) -> bytes: ...
