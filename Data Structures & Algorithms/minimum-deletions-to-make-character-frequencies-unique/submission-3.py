class Solution:
    def minDeletions(self, s: str) -> int:
        freq = {}
        same = set()
        counter = 0

        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        for x, y in freq.items():
            while y in same and y != 0:
                counter += 1
                y -= 1
            if y > 0:
                same.add(y)
        return counter

        pass
