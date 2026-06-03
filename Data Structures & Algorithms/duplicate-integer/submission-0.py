class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hsh = {}
        for num in nums:
            if num not in hsh.keys():
                hsh[num] = 1
            else:
                return True
        return False
