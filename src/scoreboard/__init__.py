import sys

from cpu import Cpu
from utils import parse


def main() -> None:
    path = ""
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        print("Uso:")
        print(f"\t{sys.argv[0]} example.s")
        sys.exit(-1)

    operations = parse(path)

    cpu = Cpu(operations)
    cpu.start()
    cpu.inst_table.print()
