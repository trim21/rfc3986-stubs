from .api import (
    iri_reference,
    is_valid_uri,
    normalize_uri,
    uri_reference,
    urlparse,
)
from .iri import IRIReference
from .parseresult import ParseResult as ParseResult
from .uri import URIReference

__all__ = [
    "IRIReference",
    "ParseResult",
    "URIReference",
    "__author__",
    "__author_email__",
    "__copyright__",
    "__license__",
    "__title__",
    "__version__",
    "iri_reference",
    "is_valid_uri",
    "normalize_uri",
    "uri_reference",
    "urlparse",
]

__title__: str
__author__: str
__author_email__: str
__license__: str
__copyright__: str
__version__: str
