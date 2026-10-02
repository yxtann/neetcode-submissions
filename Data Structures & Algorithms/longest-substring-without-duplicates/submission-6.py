class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_pointer = 0
        char_set = set()
        longest = 0

        for right_pointer, char in enumerate(s):
            while char in char_set:
                char_set.remove(s[left_pointer])
                left_pointer += 1
            char_set.add(char)
            if len(char_set) > longest:
                longest = len(char_set)
        
        return longest