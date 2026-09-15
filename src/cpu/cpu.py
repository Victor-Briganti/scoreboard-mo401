from memory import FetchUnit
from tables import FunctionalStatus, InstructionStatus, RegisterStatus


class Cpu:
    def __init__(self, instructions):
        self.func_table = FunctionalStatus()
        self.reg_table = RegisterStatus()
        self.inst_table = InstructionStatus(instructions)
        self.fetch = FetchUnit(instructions)

    def _issue() -> None:
        return

    def _read() -> None:
        return

    def _execute() -> None:
        return

    def _write() -> None:
        return

    def start() -> None:
        return

    def print(self) -> None:
        print("Aqui")
