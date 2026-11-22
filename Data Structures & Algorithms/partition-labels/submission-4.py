class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        start = 0
        end = 0
        result = []

        for i in range(len(s)):
            last[s[i]] = i
        
        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                result.append(i - start + 1)
                start = i + 1
        return result


                
        