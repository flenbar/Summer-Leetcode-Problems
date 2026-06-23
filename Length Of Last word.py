class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        counts = 0
        i = -1
        while s[i] != " ":
            counts += 1
            i -= 1
            if abs(i) > len(s):
                break
        return counts
