from dataclasses import dataclass

from memory import Operation


@dataclass
class InstRow:
    issue: int | None
    read: int | None
    exec: int | None
    write: int | None


class InstructionStatus:
    def __init__(self, operations: list[Operation]):
        self.table: dict[str, InstRow] = {}
        for op in operations:
            self.table[op.inst] = InstRow(None, None, None, None)

    def print(self):
        headers = [
            "Instruction",
            "Issue",
            "Read Operands",
            "Exec Comp",
            "Write Result",
        ]
        widths = [15, 8, 15, 12, 14]

        header_str = (
            "| "
            + " | ".join(
                f"{h:<{w}}" if i == 0 else f"{h:^{w}}"
                for i, (h, w) in enumerate(zip(headers, widths))
            )
            + " |"
        )
        separator_str = (
            "|"
            + "|".join(
                f":{'-' * w}-" if i == 0 else f":{'-' * w}:"
                for i, w in enumerate(widths)
            )
            + "|"
        )

        print(header_str)
        print(separator_str)

        for inst, row in self.table.items():
            vals = [
                str(inst),
                str(row.issue) if row.issue is not None else "none",
                str(row.read) if row.read is not None else "none",
                str(row.exec) if row.exec is not None else "none",
                str(row.write) if row.write is not None else "none",
            ]

            row_str = (
                "| "
                + " | ".join(
                    f"{val:<{w}}" if i == 0 else f"{val:^{w}}"
                    for i, (val, w) in enumerate(zip(vals, widths))
                )
                + " |"
            )
            print(row_str)
