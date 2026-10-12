class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = set(range(len(nums) + 1))
        actual = set(nums)

        return(expected - actual).pop()
        