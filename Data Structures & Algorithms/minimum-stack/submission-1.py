class MinStack:

    def __init__(self):
        self.stack = [] # starts empty 
        # create another where minStack min element will be minStack[-1] 
        self.minStack = [] 


    def push(self, val: int) -> None:
        # stack might be empty when adding elements to the list 
        # pushes element onto the list .append()? O(1) time? 
        self.stack.append(val)
        # if new value is smaller than current minimum
        if self.minStack and val < self.minStack[-1]:
            # push new value 
            self.minStack.append(val)
        # if new value is larger then current minimum 
        elif self.minStack and val > self.minStack[-1]:
            # push current minimum? 
            self.minStack.append(self.minStack[-1])
        else: 
            # when stack is empty only used once
            self.minStack.append(val)
        
            
         
    def pop(self) -> None:
        # Stack will have something inside 
        # removes the top item on the stack stack[-1]
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # Stack will have something inside 
        # gets the item on the top of the stack same as peek. Whats the current value on stack 
        # print stack[-1]
        return self.stack[-1]

    def getMin(self) -> int:
        # Stack will have something inside
        # Create another stack which the top element will always be the lowest element from the first stack 
        # return MinStack 
        return self.minStack[-1]
