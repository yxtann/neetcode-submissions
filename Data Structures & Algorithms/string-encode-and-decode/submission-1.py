class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_string = ""
        for string in strs:
            len_string = str(len(string))
            enc_string += len_string
            enc_string += ("*")
            enc_string += (string)
        return enc_string

    def decode(self, s: str) -> List[str]:
        i = 0
        str_len = ""
        strs = []

        while i < len(s):
            while s[i] != "*":
                str_len += s[i]
                i += 1
            str_len = int(str_len)

            # Add one to skip the delimiter
            strs.append(s[i+1:i+str_len+1])

            # Jump to the start of the next number
            i += str_len + 1

            # Reset str_len
            str_len = ""
            
        return strs

