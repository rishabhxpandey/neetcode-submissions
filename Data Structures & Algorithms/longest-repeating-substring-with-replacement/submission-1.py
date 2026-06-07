class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        approach:

        - some sort of sliding window
        - keep track of length of window
        - keep track of how many times the max element occurs
        - have a dct to keep track of element occurrence
        - reduce window size when num of replacements = 0
        '''

        tracker = {}
        max_len = 0
        max_elem_count = 0
        left = 0

        # BAAA
        '''
        tracker {
            A: 0
            B: 1
        } k = 0
        max_elem_count = 4
        window_len = 5
        max_len = 5


        '''

        for right in range(len(s)):
            # only have tracker for window len
            tracker[s[right]] = 1 + tracker.get(s[right], 0)
            max_elem_count = max(max_elem_count, tracker[s[right]])

            # shrinking the window
            while (right-left+1) - max_elem_count > k: # condition
                #update tracker
                tracker[s[left]] -= 1

                left += 1

            # update max_len
            window_len = right-left + 1
            max_len = max(max_len, window_len)

        return max_len