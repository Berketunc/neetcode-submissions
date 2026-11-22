class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = nums[0]
        running = 0

        for n in nums:
            if running < 0:
                running = 0
            running += n   
            largest = max(largest, running)
        return largest
        



        