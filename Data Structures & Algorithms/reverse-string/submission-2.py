class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start_pointer = 0
        end_pointer = len(s) - 1

        while start_pointer <= end_pointer:
            left_char = s[start_pointer]
            right_char = s[end_pointer]
            s[start_pointer] = right_char
            s[end_pointer] = left_char

            start_pointer += 1
            end_pointer -= 1
        
        return s