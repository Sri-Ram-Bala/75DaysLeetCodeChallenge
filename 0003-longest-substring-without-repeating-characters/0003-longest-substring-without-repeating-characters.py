class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Stores the last seen index of each character
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            current_char = s[right]
            
            # If the character is in the map and within the current window
            if current_char in char_map and char_map[current_char] >= left:
                # Move the left pointer to the right of the previous occurrence
                left = char_map[current_char] + 1
            
            # Update the last seen index of the character
            char_map[current_char] = right
            
            # Calculate the current window size and update max_length
            max_length = max(max_length, right - left + 1)
            
        return max_length