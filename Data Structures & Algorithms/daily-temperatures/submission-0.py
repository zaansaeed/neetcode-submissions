class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)

        stack = []

        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((temp, i))
            else:
                while stack and temp > stack[-1][0]:
                    idx = stack[-1][1]
                    num_days = i - idx
                    res[idx] = num_days
                    stack.pop()
                stack.append((temp, i))
        return res
