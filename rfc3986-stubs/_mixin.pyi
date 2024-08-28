from typing import TypedDict, Self

from typing_extensions import deprecated

from .uri import URIReference

class _AuthorityInfo(TypedDict):
    userinfo: str | None
    host: str | None
    port: str | None

class URIMixin:
    scheme: str | None
    authority: str | None
    path: str | None
    query: str | None
    fragment: str | None
    encoding: str

    def authority_info(self) -> _AuthorityInfo: ...
    @property
    def host(self) -> str | None: ...
    @property
    def port(self) -> str | None: ...
    @property
    def userinfo(self) -> str | None: ...
    def is_absolute(self) -> bool: ...
    @deprecated('since 1.1.0')
    def is_valid(self, **kwargs: bool) -> bool: ...
    @deprecated('since 1.1.0')
    def authority_is_valid(self, require: bool = False) -> bool: ...
    @deprecated('since 1.1.0')
    def scheme_is_valid(self, require: bool = False) -> bool: ...
    @deprecated('since 1.1.0')
    def path_is_valid(self, require: bool = False) -> bool: ...
    @deprecated('since 1.1.0')
    def query_is_valid(self, require: bool = False) -> bool: ...
    @deprecated('since 1.1.0')
    def fragment_is_valid(self, require: bool = False) -> bool: ...
    def normalized_equality(self, other_ref: URIReference) -> bool: ...
    def resolve_with(
        self, base_uri: str | URIReference, strict: bool = False
    ) -> Self: ...
    def unsplit(self) -> str: ...
    def copy_with(
        self,
        scheme: str | None = ...,
        authority: str | None = ...,
        path: str | None = ...,
        query: str | None = ...,
        fragment: str | None = ...,
    ) -> Self: ...
