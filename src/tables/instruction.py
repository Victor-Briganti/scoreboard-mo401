from dataclasses import dataclass


@dataclass
class InstRow:
    inst: str
    issue: int
    read: int
    exec: int
    write: int
