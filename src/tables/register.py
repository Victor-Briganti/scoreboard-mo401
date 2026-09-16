from utils import REGISTERS


class RegisterStatus:
    def __init__(self):
        self.table: dict[str, str | None] = {}
        for reg in REGISTERS:
            self.table[reg] = None

        self.new_table = self.table.copy()

    def get(self, reg) -> str | None:
        return self.table.get(reg)

    def set(self, reg, fu):
        self.new_table[reg] = fu

    def update(self):
        self.table = self.new_table.copy()

    def print(self):
        headers = ["Register", "Unit"]
        widths = [10, 10]

        # Cabeçalho no estilo markdown
        header_str = (
            "| " + " | ".join(f"{h:<{w}}" for h, w in zip(headers, widths)) + " |"
        )
        separator_str = "|" + "|".join("-" * (w + 2) for w in widths) + "|"


        table = ""
        for reg, fu in self.table.items():
            if fu is None:
                continue

            fu_str = str(fu)
            row_str = f"| {reg:<{widths[0]}} | {fu_str:<{widths[1]}} |\n"
            table += row_str

        print(header_str)
        print(separator_str)
        if table != "":
            print(table)

