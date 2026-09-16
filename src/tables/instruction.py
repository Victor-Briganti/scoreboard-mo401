from dataclasses import dataclass

from memory import Operation

SHOW_ADDRESS = False


@dataclass
class InstRow:
    inst: str
    issue: int | None
    read: int | None
    exec: int | None
    write: int | None
    exec_counter: int | None


class InstructionStatus:
    def __init__(self, operations: list[Operation]):
        self.table: dict[str, InstRow] = {}
        for op in operations:
            self.table[op.address] = InstRow(op.inst, None, None, None, None, None)

        self.new_table = self.table.copy()

    def get(self, address: str) -> InstRow:
        return self.table[address]

    def update_issue(self, address: str, cycle: int):
        self.new_table[address].issue = cycle

    def update_read(self, address: str, cycle: int):
        self.new_table[address].read = cycle

    def update_write(self, address: str, cycle: int):
        self.new_table[address].write = cycle

    def update_exec(self, address: str, cycle: int, fu_cycles: int):
        if self.table[address].exec is None:
            self.new_table[address].exec = cycle
            self.new_table[address].exec_counter = fu_cycles - 1
        else:
            self.new_table[address].exec = self.table[address].exec + 1
            self.new_table[address].exec_counter = self.table[address].exec_counter - 1

    def update(self):
        self.table = self.new_table.copy()

    def print(self):
        if SHOW_ADDRESS:
            headers = [
                "Address",
                "Instruction",
                "Issue",
                "Read Operands",
                "Exec Comp",
                "Write Result",
            ]
            widths = [8, 15, 8, 15, 12, 14]
        else:
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

        for address, row in self.table.items():
            vals = [
                str(row.issue) if row.issue is not None else "none",
                str(row.read) if row.read is not None else "none",
                str(row.exec) if row.exec is not None else "none",
                str(row.write) if row.write is not None else "none",
            ]

            if SHOW_ADDRESS:
                vals = [address, str(row.inst)] + vals
            else:
                vals = [str(row.inst)] + vals

            row_str = (
                "| "
                + " | ".join(
                    f"{val:<{w}}" if i == 0 else f"{val:^{w}}"
                    for i, (val, w) in enumerate(zip(vals, widths))
                )
                + " |"
            )
            print(row_str)
