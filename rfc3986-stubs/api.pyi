from .iri import IRIReference
from .parseresult import ParseResult
from .uri import URIReference

def uri_reference(uri: str | bytes, encoding: str = ...) -> URIReference: ...
def iri_reference(iri: str | bytes, encoding: str = ...) -> IRIReference: ...
def is_valid_uri(
    uri: str | bytes,
    encoding: str = ...,
    require_scheme: bool = ...,
    require_authority: bool = ...,
    require_path: bool = ...,
    require_query: bool = ...,
    require_fragment: bool = ...,
    **kwargs: bool,
) -> bool: ...
def normalize_uri(uri: str | bytes, encoding: str = ...) -> str: ...
def urlparse(uri: str | bytes, encoding: str = ...) -> ParseResult: ...
