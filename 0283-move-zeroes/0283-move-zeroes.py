class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        hole=0
        for i in range (len(nums)):
            if nums[i]!=0:
                nums[hole],nums[i]=nums[i],nums[hole]
                hole+=1



