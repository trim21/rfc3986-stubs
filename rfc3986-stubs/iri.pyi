import typing as t

from rfc3986._mixin import URIMixin
from rfc3986 import URIReference
from typing import Self

from rfc3986.misc import URIReferenceBase

class IRIReference(URIReferenceBase, URIMixin):
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
    @classmethod
    def from_string(cls, iri_string: str | bytes, encoding: str = ...) -> Self: ...
    def encode(
        self, idna_encoder: t.Callable[[str], str | bytes] | None = None
    ) -> URIReference: ...
