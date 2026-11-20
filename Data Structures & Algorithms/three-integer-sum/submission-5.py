class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sorted_nums = sorted(nums)                      # sort so two pointers work

        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue                                # skip duplicate i

            l, r = i + 1, len(sorted_nums) - 1          # reset pointers for each i
            while l < r:                                # keep moving until they meet
                total = sorted_nums[i] + sorted_nums[l] + sorted_nums[r]
                if total < 0:
                    l += 1                              # too small, so increase
                elif total > 0:
                    r -= 1                              # too big, so decrease
                else:
                    result.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    l += 1                              # move off this triplet
                    while l < r and sorted_nums[l] == sorted_nums[l - 1]:
                        l += 1                          # skip duplicate l
        return result