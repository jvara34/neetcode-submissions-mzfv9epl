class Solution:
    def isValid(self, s: str) -> bool:
        # create a stack 
        stack = [] 
        # create a map which maps the closed and the open brackets 
        hashmap = {')' : '(', ']' : '[', '}' : '{'} 
        # Key, close, value -> open 

        # Everytime there is a closed value it needs to make sure that the stack matches with open value 

        # ['()']


        # loop through the string 
        for char in s: 
            # check current character is in the map 
            if char in hashmap: # making sure that the key is hashmap 
                # check if stack is not empty AND check if top of stack == hashmap value 
                if stack and stack[-1] == hashmap[char]:
                    # if correct then pop the value from the stack 
                    stack.pop() 
                # else 
                else: 
                    # reuturn false 
                    return False
            # else:
            else: 
                # stack.append(c)
                stack.append(char)
            
        # return true if Stack is empty
        if stack: # checks if stack is has something
            return False
        else: 
            return True
        
        