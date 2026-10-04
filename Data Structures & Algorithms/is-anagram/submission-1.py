class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = sorted(list(s))
        set_t = sorted(list(t))

        if set_s == set_t:
            return True
        else:
            return False
        