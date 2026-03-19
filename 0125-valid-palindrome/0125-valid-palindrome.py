class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = list(s)
        i = 0
        while i < len(s):
            if s[i].isalpha() or s[i].isdigit():
                i += 1
            else:
                s.pop(i)
        s=''.join(s)
        print(s)
        if s == s[::-1]:
            return True
        else:
            return False
