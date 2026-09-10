class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {c: 0 for c in s}
        dict2 = {c: 0 for c in t}
        for c in s:
            dict1[c] += 1
        for c in t:
            dict2[c] +=1
        return dict1 == dict2