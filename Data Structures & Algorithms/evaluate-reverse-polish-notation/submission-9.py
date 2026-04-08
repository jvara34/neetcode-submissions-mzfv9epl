import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Understanding 
            # every operator is benhind the two digits instead of middle 
            # 1 2 + -> 1 + 2 
            # 4 - -> ... - 4 
            # Solved from the left to right 

        # iterate through tokens 
            # if token is int 
                # then push onto stack 
            # if token is operator then
                # pop two items from the stack 
                # use current operator for the equation 
                # push item onto the stack 

        stack = [] 
        hashmap = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

        for i in range(len(tokens)):

            if tokens[i] not in hashmap: 
                stack.append(int(tokens[i]))
            else:
                x = stack.pop()
                y = stack.pop()
                result = hashmap[tokens[i]](y, x) # result will have the amount of current operator PUSH to stack
                stack.append(int(result))

            
        return stack[-1]
