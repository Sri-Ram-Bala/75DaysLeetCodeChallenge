class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        l,r,sum = 0,0,0
        maxsum = float('-inf')
        for num in nums:
            sum = sum + num
            if r-l+1 == k:
                maxsum = max(sum, maxsum)
                sum -= nums[l]
                l+=1
            r+=1
        max_avg = maxsum/k
        return max_avg