class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_letters = defaultdict(int)
        s2_letters = defaultdict(int)
        if len(s2) < len(s1):
            return False

        for i in range(len(s1)):
            s1_letters[s1[i]] += 1
            s2_letters[s2[i]] += 1

        l = 0
        if s1_letters == s2_letters:
            return True

        for r in range(len(s1), len(s2)):
            s2_letters[s2[l]] -= 1
            if s2_letters[s2[l]] == 0:
                del s2_letters[s2[l]]
            s2_letters[s2[r]] += 1
            l += 1
            if s1_letters == s2_letters:
                return True

        return False




        
                 

         
   


        