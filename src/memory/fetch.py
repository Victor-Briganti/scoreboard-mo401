from .operation import Operation


class FetchUnit:
    def __init__(self, ops: list[Operation]):
        self.mem = ops
        self.pos = 0
        self._locked = False

    def next(self) -> Operation | None:
        if self._locked or self.pos == len(self.mem):
            return None

        op = self.mem[self.pos]
        self.pos = self.pos + 1
        return op

    def lock(self):
        self._locked = True

    def unlock(self):
        self._locked = False
