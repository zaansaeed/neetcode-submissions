class MinStack:
    def __init__(self):
        self._stack = []

    def push(self, val: int) -> None:
        cur_min = val if not self._stack else min(val, self._stack[-1][1])
        self._stack.append((val, cur_min))

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1][0]

    def getMin(self) -> int:
        return self._stack[-1][1]