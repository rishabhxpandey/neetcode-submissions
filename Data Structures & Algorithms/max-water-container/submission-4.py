class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        area = min(two pointers) * width
        width = (r-l)

        initialize l at 0, r at end

        whichever one is smaller, move that ptr

        height=[1,7,2,5,12,3,500,500,7,8,4,7,3,6]
                                            ^
        '''
        l, r = 0, len(heights)-1
        max_area = 0

        while l < r:
            curr_area = min(heights[l], heights[r]) * (r-l)
            max_area = max(max_area, curr_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area