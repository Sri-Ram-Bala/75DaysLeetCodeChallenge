class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic_freq = {}
        for num in nums:
            if num in dic_freq:
                dic_freq[num] += 1
            else:
                dic_freq[num] = 1
        dic_freq = dict(sorted(dic_freq.items(), key=lambda x: x[1], reverse=True))
        k_frequent = []
        for key, val in dic_freq.items():
            if k==0:
                break
            k_frequent.append(key)
            k -= 1
        return k_frequent
