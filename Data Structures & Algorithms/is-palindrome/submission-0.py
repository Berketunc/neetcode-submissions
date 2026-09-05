class Solution:
    def isPalindrome(self, s: str) -> bool:
        ordered = ""
        for c in s:
            if c.isalnum():
                ordered += c.lower()
        return ordered == ordered[::-1]
        
        