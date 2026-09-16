from dataclasses import dataclass

from memory import Operation
from utils import FUNCTION_UNITS, INST_TO_FU


@dataclass
class FuncRow:
    busy: bool
    op: str
    fi: str | None
    fj: str | None
    fk: str | None
    qj: str | None
    qk: str | None
    rj: bool
    rk: bool


class FunctionalStatus:
    def __init__(self):
        self.table: dict[str, FuncRow | None] = {}
        self.inst_to_fu: dict[str, list[str]] = INST_TO_FU
        for key, value in FUNCTION_UNITS.items():
            if value[0] != 1:
                keys: list[str] = []
                for i in range(value[0]):
                    keys.append(key + str(i))
                    self.table[keys[-1]] = None

                self.inst_to_fu = {
                    inst: keys if fu == key else [fu]
                    for inst, fu in self.inst_to_fu.items()
                }
            else:
                self.table[key] = None

    def get(self, fu: str) -> FuncRow:
        return self.table[fu]

    def get_empty(self, opcode: str) -> str | None:
        fus = self.inst_to_fu[opcode]

        for und in fus:
            if self.table[und] is None:
                return und

        return None

    def insert(
        self,
        fu: str,
        busy: bool,
        op: str,
        fi: str | None,
        fj: str | None,
        fk: str | None,
        qj: str | None,
        qk: str | None,
    ) -> None:
        rj = qj is None
        rk = qk is None

        row = FuncRow(busy, op, fi, fj, fk, qj, qk, rj, rk)
        self.table[fu] = row

    def update(
        self,
        fu: str,
        row: FuncRow,
    ) -> None:
        self.table[fu] = row

    def reset_q(self, fu: str) -> None:
        for value in self.table.values():
            if value is not None:
                if value.qj == fu:
                    value.qj = None
                    value.rj = True

                if value.qk == fu:
                    value.qk = None
                    value.rk = True

    def remove(self, fu: str) -> None:
        self.table[fu] = None

    def can_write(self, op: Operation) -> bool:
        # Verica se existe um WAR
        for fu, row in self.table.items():
            if (
                row is not None
                and op.fu != fu
                and ((row.fj == op.rd and row.rj) or (row.fk == op.rd and row.rk))
            ):
                return False
        return True

    def print(self):
        headers = ["unit", "busy", "op", "fi", "fj", "fk", "qj", "qk", "rj", "rk"]
        widths = [10, 5, 6, 4, 4, 4, 8, 8, 5, 5]

        # Cabeçalho no estilo markdown
        header_str = (
            "| " + " | ".join(f"{h:<{w}}" for h, w in zip(headers, widths)) + " |"
        )
        separator_str = "|" + "|".join("-" * (w + 2) for w in widths) + "|"

        print(header_str)
        print(separator_str)

        for key, value in self.table.items():
            # Se a entrada for vazia replica em cada uma das entradas
            if value is None:
                row_data = [key] + ["none"] * 9
            else:
                row_data = [
                    key,
                    value.busy,
                    value.op,
                    value.fi,
                    value.fj,
                    value.fk,
                    value.qj,
                    value.qk,
                    value.rj,
                    value.rk,
                ]

            formatted_data = [
                "none" if item is None else str(item) for item in row_data
            ]

            row_str = (
                "| "
                + " | ".join(f"{item:<{w}}" for item, w in zip(formatted_data, widths))
                + " |"
            )
            print(row_str)
