class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Q:
        - Any time/space considerations?
        - Lowercase only? c == C

        approach:
        - use the counter module to find the count of each char in the str
        - compare hashmaps

        - if space considerations:
            - sort both strings and compare incremental chars
        '''

        if len(s) != len(t): return False
        
        s_counter, t_counter = {}, {}

        for char in s:
            if char not in s_counter:
                s_counter[char] = 1
            else:
                s_counter[char] += 1

        for char in t:
            if char not in t_counter:
                t_counter[char] = 1
            else:
                t_counter[char] += 1
            
        return s_counter == t_counter
