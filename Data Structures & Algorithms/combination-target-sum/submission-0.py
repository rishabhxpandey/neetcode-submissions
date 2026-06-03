class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def dfs(start, path, curr_sum):
            if curr_sum == target:
                output.append(path[:])
                return
            
            if curr_sum > target:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i, path, nums[i] + curr_sum)
                path.pop()

        dfs(0, [], 0)
        return output

