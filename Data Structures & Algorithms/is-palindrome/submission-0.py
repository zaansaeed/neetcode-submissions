class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = "".join([char for char in s if char.isalnum()])
        cleaned_text = cleaned_text.lower()

        l = 0
        r = len(cleaned_text) - 1

        while l < r:
            if cleaned_text[l] == cleaned_text[r]:
                l += 1 
                r -= 1
            else:
                return False
        
        return True
        
        


