class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        match = 0
        i = 0
        expected=sorted(heights)

        for i, x in enumerate(heights):
            if expected[i] != x:
                match +=1
        return match
        