class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter_dict = {
            letter: 0 for letter in "abcdefghijklmnopqrstuvwxyz".upper()
        }

        # pointers
        left_ptr = 0
        right_ptr = 0

        # counters
        longest_substring = 0
        max_same_char = 0

        for right_ptr, char in enumerate(s):

            # add char to window and update the counter_dict
            counter_dict[char] += 1
            max_same_char = max(counter_dict[char], max_same_char)
            curr_str_length = right_ptr - left_ptr + 1

            """
            Check window validity by comparing the window (curr_str_length) with the budget
            increase left_ptr by 1 until the window is valid again

            If the curr_str_length is more than max_same_char + k, the only reason is because we need to change
            more than k chars, thus the window is invalid.
            """
            while curr_str_length > (max_same_char + k) and left_ptr < right_ptr:

                # when incrementing the left_ptr, also reduce the char count of what was the left_ptr pointing to
                counter_dict[s[left_ptr]] -= 1 
                left_ptr += 1
                curr_str_length = right_ptr - left_ptr + 1


            # Update the max string length
            if curr_str_length > longest_substring:
                longest_substring = curr_str_length
        
        return longest_substring
