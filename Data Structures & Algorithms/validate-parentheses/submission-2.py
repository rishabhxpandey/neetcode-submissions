class Solution:
    def isValid(self, s: str) -> bool:
        
        # iterate over list
        # if char in open
            # add to stack
        # if char in close
            # if top of stack matches
                # continue
            # if not match
                # return false

        stack = []
        mapping = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if not stack:
                    return False
                removed = stack.pop()
                if removed != mapping[char]:
                    return False
        return len(stack) == 0