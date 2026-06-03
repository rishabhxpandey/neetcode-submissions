class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Time/space complexity restrictions?

        Pseudocode:

        brute force:
        - nested for loops to iterate over each pair

        optimized:
        some hashmap that stores the index of the complement pair

        target = 7
        {
            4: 0
            3: 1
            2: 2
            1: 3
        }

        while looping if the current num exists in the hashmap, return that idx + current idx
        '''

        complement_tracker = {}

        for idx in range(len(nums)):
            num = nums[idx]
            if num in complement_tracker:
                return [complement_tracker[num], idx]
            complement_tracker[target-num] = idx
        
        return
