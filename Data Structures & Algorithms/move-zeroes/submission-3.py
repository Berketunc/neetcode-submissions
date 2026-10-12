class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        total = []

        for i, x in enumerate(nums):
            if x != 0:
                total.append(x)
        
        for i in range(len(nums)):
            if i < len(total):
                nums[i] = total[i]
            else:
                nums[i] = 0
            
                
            
                
        