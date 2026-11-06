class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        fqs = {}

        for idx in range(0,len(s)):
            fqs[s[idx]] = fqs.get(s[idx], 0) + 1
            fqs[t[idx]] = fqs.get(t[idx], 0) - 1
        
        for value in fqs.values():
            if value != 0:
                return False

        return True
        