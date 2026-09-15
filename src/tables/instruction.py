from dataclasses import dataclass


@dataclass
class InstRow:
    inst: str
    issue: int | None
    read: int | None
    exec: int | None
    write: int | None
