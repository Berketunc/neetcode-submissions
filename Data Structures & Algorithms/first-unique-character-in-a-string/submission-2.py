class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            repeated = False
            for j in range(len(s)):
                if i != j and s[i] == s[j]:
                    repeated = True
                    break
            if not repeated:
                return i
        return -1