class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        
        
        maxSub = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        set_checker = {s[l]}

        while r < len(s):
            if s[r] not in set_checker:
                set_checker.add(s[r])
                r += 1
            else:
                set_checker.remove(s[l])
                l += 1
            if len(set_checker) > maxSub:
                maxSub = len(set_checker)
        
        return maxSub

