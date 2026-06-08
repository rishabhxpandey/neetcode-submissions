class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Once you sort the given array, this turns into 2 sum

        '''

        nums.sort()
        res = set()
        
        for fixed in range(len(nums)-2):
            
            l = fixed + 1
            r = len(nums)-1

            while l < r:
                if nums[l] + nums[r] == -1 * nums[fixed]:
                    res.add((nums[fixed], nums[l], nums[r]))
                    l+=1
                elif nums[l] + nums[r] > -1 * nums[fixed]:
                    r -= 1
                else:
                    l += 1

        return [list(item) for item in res]
