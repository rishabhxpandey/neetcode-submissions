class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        - if len <= 1:
            - return len
        
        - approach:
            - keep a set() to track elements in window
            - l/r pointers
            - if new elem is in set, move l pointer up until its not
            - have var to track max_len
             |         
        "zxyzxyz"
           ^
        "abcbcbb"
        set = (a,b,c)

        '''

        if len(s) <= 1:
            return len(s)

        l = 0
        element_set = set()
        max_len = 0

        for r in range(len(s)):
            if s[r] not in element_set:
                max_len = max(r-l + 1, max_len)
                element_set.add(s[r])
            else:
                while l < r and s[l] != s[r]:
                    element_set.remove(s[l])
                    l += 1
                l+=1
        
        return max_len


