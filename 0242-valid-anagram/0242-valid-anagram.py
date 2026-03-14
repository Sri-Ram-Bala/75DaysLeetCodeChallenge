class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_s={}
        for char in s:
            if char in chars_s:
                chars_s[char] += 1
            else:
                chars_s[char] = 1
        for char in t:
            if char not in chars_s:
                return False
            else:
                chars_s[char] -= 1
        val = chars_s.values()
        for v in val:
            if v != 0:
                return False
        return True 