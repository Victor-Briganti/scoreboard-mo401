import re

from memory import FetchUnit, Operation
from tables import FunctionalStatus, InstructionStatus, RegisterStatus
from utils import FUNCTION_UNITS, REGISTERS


class Cpu:
    def __init__(self, instructions: list[Operation]):
        self.func_table = FunctionalStatus()
        self.reg_table = RegisterStatus()
        self.inst_table = InstructionStatus(instructions)
        self.fetch = FetchUnit(instructions)
        self.cycle: int = 0

        # Lista de operações sendo executadas
        self.queue: list[Operation] = []

    def _issue(self) -> None:
        op = self.fetch.peek()

        # Verifica se existe um WAW
        if self.reg_table.get(op.rd) is None:
            # Reserva unidade funcional
            fu = self.func_table.get_empty(op.opcode)
            if fu is None:
                return

            # Atualiza tabela de registradores
            qj = self.reg_table.get(op.rs1)
            qk = self.reg_table.get(op.rs2)
            if op.rd in REGISTERS:
                self.reg_table.set(op.rd, fu)

            self.func_table.insert(fu, True, op.opcode, op.rd, op.rs1, op.rs2, qj, qk)

            # Adiciona a instrução da fila de execução da CPU
            op.fu = fu
            self.queue.append(op)
            self.inst_table.update_issue(op.inst, self.cycle)

            self.fetch.pop()
            return

    def _read(self, op: Operation) -> None:
        # Verifica se o Rk e o Rj já podem ser lidos.
        row = self.func_table.get(op.fu)
        if row.rk and row.rj:
            row.rk = False
            row.rj = False
            self.func_table.update(op.fu, row)

        self.inst_table.update_read(op.inst, self.cycle)

    def _execute(self, op: Operation) -> None:
        inst = self.inst_table.get(op.inst)
        fu = re.sub(r"\d", "", op.fu)
        self.inst_table.update_exec(inst, self.cycle, FUNCTION_UNITS[fu][1])

    def _write(self, op: Operation) -> None:
        self.inst_table.update_write(op.inst, self.cycle)

        # Limpa as tabelas de status
        if op.rd in REGISTERS:
            self.reg_table.set(op.rd, None)
            self.func_table.reset_q(op.fu)
            self.func_table.remove(op.fu)

    def start(self) -> None:
        while True:
            self.cycle = self.cycle + 1

            if self.fetch.is_empty():
                return

            self._issue()
            for op in self.queue:
                inst = self.inst_table.get(op.inst)

                if inst.read is None:
                    self._read(op)
                elif inst.exec is None or inst.exec_counter != 0:
                    self._execute(op)
                else:
                    self._write(op)

    def print(self) -> None:
        print("Aqui")
