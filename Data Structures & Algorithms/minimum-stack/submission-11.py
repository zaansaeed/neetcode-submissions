class MinStack:

    def __init__(self):
        self._stack = deque([])
        self.current_min = None


    def push(self, val: int) -> None:
        if self.current_min is None:
            self.current_min = val

        if val < self.current_min:
            self.current_min = val
        self._stack.append((val, self.current_min))


    def pop(self) -> None:
        value, min = self._stack.pop()
        if self._stack:
            _, new_min = self._stack[-1]
        else:
            new_min = None
        self.current_min = new_min 

    def top(self) -> int:
        value, min = self._stack[-1]
        return value

    def getMin(self) -> int:
        return self.current_min
        
