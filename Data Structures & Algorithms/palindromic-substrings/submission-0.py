class Solution:
    def countSubstrings(self, s: str) -> int:
        _sum = 0

        # base_case
        if len(s) == 1: return 1

        # first let's do odd length strings
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                _sum += 1
                l -= 1
                r += 1
        
        # next let's do even length strings
        for i in range(len(s)-1):
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                _sum += 1
                l -= 1
                r += 1
                
        return _sum
                

