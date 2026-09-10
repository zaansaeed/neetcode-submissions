class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque([])
        open = ("(", "{", "[")
        valid = ("()", "{}", "[]")
    
        for char in s:
            if char in open:
                stack.append(char)
            else:
                open_char = stack.pop() if stack else ""
                temp = open_char + char
                if temp in valid:
                    continue
                else:
                    return False
        if stack:
            return False
        return True