from dataclasses import dataclass


@dataclass
class Operation:
    inst: str
    opcode: str
    rd: str
    rs1: str
    rs2: str
