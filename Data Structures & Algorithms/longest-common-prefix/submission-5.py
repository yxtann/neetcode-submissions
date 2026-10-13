class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]

        for i, char in enumerate(first_word):
            for string in strs:
                if i == len(string):
                    return first_word[:i]
                if char != string[i]:
                    return first_word[:i]
                    break

        return first_word
        
