class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = sorted(nums)
        nums = set(nums)
        i=1
        dis_num = []
        while i < n+1:
            if i not in nums:
                dis_num.append(i)
            i+=1
        return dis_num
