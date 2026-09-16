from dataclasses import dataclass


@dataclass
class Operation:
    address: str
    inst: str
    opcode: str
    rd: str
    rs1: str
    rs2: str
    fu: str | None
