from .uri import URIReference
from .iri import IRIReference
from .api import (
    iri_reference,
    is_valid_uri,
    normalize_uri,
    uri_reference,
    urlparse,
)
from .parseresult import ParseResult as ParseResult

__all__ = [
    "ParseResult",
    "URIReference",
    "IRIReference",
    "is_valid_uri",
    "normalize_uri",
    "uri_reference",
    "iri_reference",
    "urlparse",
    "__title__",
    "__author__",
    "__author_email__",
    "__license__",
    "__copyright__",
    "__version__",
]

__title__: str
__author__: str
__author_email__: str
__license__: str
__copyright__: str
__version__: str
