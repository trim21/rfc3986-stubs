import typing as t

__all__ = ["to_bytes", "to_str"]

@t.overload
def to_str(b: str | bytes, encoding: str = ...) -> str: ...
@t.overload
def to_str(b: None, encoding: str = ...) -> None: ...
@t.overload
def to_bytes(s: str | bytes, encoding: str = ...) -> bytes: ...
@t.overload
def to_bytes(s: None, encoding: str = ...) -> None: ...