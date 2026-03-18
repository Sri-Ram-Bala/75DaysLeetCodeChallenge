class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Get the length of the array
        num = len(nums)
        #Generate the prifix array
        pre = [1]*num
        for i in range(1,num):
            pre[i] = pre[i-1] * nums[i-1]
        #Generate the suffix array
        post = [1]*num
        for i in range(num-2,-1,-1):
            post[i] = post[i+1] * nums[i+1]
        #Generate result by multiplying pre*post for all i
        return [a*b for a,b in zip(pre,post)]
