class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        while j < len(nums):
            number = nums[i]
            if number == nums[j]:
                nums.pop(j)
            else:
                i += 1
                j += 1
        return len(nums)
