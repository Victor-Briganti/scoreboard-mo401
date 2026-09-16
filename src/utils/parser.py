import re
import sys

from memory import Operation
from utils import INSTRUCTIONS, REGISTERS


def parse_op(data: str, address: str = "0x0001") -> Operation:
    token = data.replace(",", "").split()

    opcode: str = token[0]
    rd: str = ""
    rs1: str = ""
    rs2: str = ""

    if opcode not in INSTRUCTIONS:
        print(f"{opcode} não é uma instrução válida")
        sys.exit(-1)

    # Parse da 'fld'
    if opcode == INSTRUCTIONS[0]:
        rd = token[1]
        if rd not in REGISTERS:
            print(f"{rd} não é um registrador válido na arquitetura")
            sys.exit(-1)

        match = re.search(r"(\d+)\(([^)]+)\)", token[2])

        if not match:
            print(f"{token[2]} não é um argumento válido na instrução {token[0]}")
            sys.exit(-1)

        imm, reg = match.groups()
        rs1 = imm
        rs2 = reg
        if rs2 not in REGISTERS:
            print(f"{rs2} não é um registrador válido na arquitetura")
            sys.exit(-1)

        return Operation(address, data, opcode, rd, rs1, rs2, None)

    # Parse da 'fsd'
    if opcode == INSTRUCTIONS[1]:
        rs1 = token[1]
        if rs1 not in REGISTERS:
            print(f"{rs1} não é um registrador válido na arquitetura")
            sys.exit(-1)

        match = re.search(r"(\d+)\(([^)]+)\)", token[2])

        if not match:
            print(f"{token[2]} não é um argumento válido na instrução {token[0]}")
            sys.exit(-1)

        imm, reg = match.groups()
        rd = imm
        rs2 = reg
        if rs2 not in REGISTERS:
            print(f"{rs2} não é um registrador válido na arquitetura")
            sys.exit(-1)

        return Operation(address, data, opcode, rd, rs1, rs2, None)

    rd = token[1]
    rs1 = token[2]
    rs2 = token[3]

    return Operation(address, data, opcode, rd, rs1, rs2, None)


def parse(path: str) -> list[Operation]:
    operations: list[Operation] = []
    with open(path, "r") as file:
        addr = 1
        for line in file:
            data = line.strip()
            if len(data) == 0:
                continue

            address = f"0x{addr:04x}"
            operations.append(parse_op(data, address))
            addr += 1

    return operations
