from dataclasses import dataclass

from utils import FUNCTION_UNITS


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
        for key, value in FUNCTION_UNITS.items():
            if value[0] != 1:
                for i in range(value[0]):
                    self.table[key + str(i)] = None
            else:
                self.table[key] = None

    def get(self, und: str) -> FuncRow:
        return self.table[und]

    def update(
        self,
        und: str,
        busy: bool,
        op: str,
        fi: str | None,
        fj: str | None,
        fk: str | None,
        qj: str | None,
        qk: str | None,
        rj,
        rk,
    ) -> None:
        row = FuncRow(busy, op, fi, fj, fk, qj, qk, rj, rk)
        self.table[und] = row

    def remove(self, und: str) -> None:
        self.table[und] = None

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
