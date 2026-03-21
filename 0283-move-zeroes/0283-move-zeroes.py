class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        hole=0
        for i,num in enumerate(nums):
            if num!=0:
                if i!=hole:
                    nums[i],nums[hole]=0,nums[i]
                hole+=1



