class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
                    "+": lambda a, b: a + b,
                    "-": lambda a, b: a - b,
                    "*": lambda a, b: a * b,
                    "/": lambda a, b: int(a / b),   # truncate toward zero
                }

        for token in tokens:
            if token in ops:
                second = stack.pop()
                first = stack.pop()
                exp = ops[token]
                result = exp(first, second)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]

        