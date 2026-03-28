class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_length = 0
        max_freq = 0
        left = 0
        
        for right in range(len(s)):
            # Add the new character to the frequency map
            count[s[right]] = 1 + count.get(s[right], 0)
            
            # Update the most frequent character count in the current window
            max_freq = max(max_freq, count[s[right]])
            
            # Current window length is (right - left + 1)
            # If replacements needed > k, shrink window from left
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
                
            # Update the global maximum length found so far
            max_length = max(max_length, right - left + 1)
            
        return max_length