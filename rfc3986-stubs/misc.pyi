import typing as t

class URIReferenceBase(t.NamedTuple):
    scheme: str | None
    authority: str | None
    path: str | None
    query: str | None
    fragment: str | None

def merge_paths(base_uri: URIReferenceBase, relative_path: str) -> str: ...

UseExisting: t.Final[object]
