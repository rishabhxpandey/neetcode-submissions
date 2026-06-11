class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = []

        '''
        [30,38,30,40,35]
        [1,2,1,0,0]

        stack =
        [(38,1), (30, 2)]
        res = 
        [1, x, ]
        '''

        for idx in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[idx]:
                temp, position = stack.pop()
                res[position] = (idx - position)
            stack.append((temperatures[idx], idx))

        return res