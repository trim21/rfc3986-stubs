from typing import Collection, Any

from rfc3986 import URIReference

class RFC3986Exception(Exception): ...

class InvalidAuthority(RFC3986Exception):
    def __init__(self, authority: str | bytes) -> None: ...

class InvalidPort(RFC3986Exception):
    def __init__(self, port: str) -> None: ...

class ResolutionError(RFC3986Exception):
    def __init__(self, uri: URIReference) -> None: ...

class ValidationError(RFC3986Exception): ...

class MissingComponentError(ValidationError):
    uri: URIReference
    components: list[str]
    def __init__(self, uri: URIReference, *component_names: str) -> None: ...

class UnpermittedComponentError(ValidationError):
    component_name: str
    component_value: Any
    allowed_values: Collection[Any]
    def __init__(
        self, component_name: str, component_value: Any, allowed_values: Collection[Any]
    ) -> None: ...

class PasswordForbidden(ValidationError):
    uri: str | URIReference
    def __init__(self, uri: str | URIReference) -> None: ...

class InvalidComponentsError(ValidationError):
    uri: URIReference
    components: list[str]
    def __init__(self, uri: URIReference, *component_names: str) -> None: ...

class MissingDependencyError(RFC3986Exception): ...
