from typing import Self

from ._mixin import URIMixin as URIMixin

from .misc import URIReferenceBase

class URIReference(URIReferenceBase, URIMixin):
    encoding: str
    def __new__(
        cls,
        scheme: str | None,
        authority: str | None,
        path: str | None,
        query: str | None,
        fragment: str | None,
        encoding: str = ...,
    ) -> Self: ...
    def __eq__(self, other: object) -> bool: ...
    def normalize(self) -> URIReference: ...
    @classmethod
    def from_string(cls, uri_string: str | bytes, encoding: str = ...) -> Self: ...
