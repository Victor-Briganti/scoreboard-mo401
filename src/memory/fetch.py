from .operation import Operation


class FetchUnit:
    def __init__(self, ops: list[Operation]):
        self.mem = ops
        self.pos = 0

    def peek(self) -> Operation | None:
        return self.mem[self.pos]

    def pop(self) -> None:
        self.pos = self.pos + 1

    def is_empty(self) -> bool:
        return self.pos == len(self.mem)
