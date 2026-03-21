class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range (len(nums)):
            if nums[i]==0:
                zero = nums.pop(i)
                nums.append(zero)

                



