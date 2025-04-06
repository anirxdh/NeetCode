#Medium

class MinStack:


   def __init__(self):
       self.stack = []
       self.minStack = []


   def push(self, val: int) -> None:
       self.stack.append(val)
       value = min(val , self.minStack[-1] if self.minStack else val)
       self.minStack.append(value)


   def pop(self) -> None:
       self.stack.pop()
       self.minStack.pop()


   def top(self) -> int:
       return self.stack[-1]


   def getMin(self) -> int:
       return self.minStack[-1]
      




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == "__main__":
    # Example usage:
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(min_stack.getMin())  # Returns -3
    min_stack.pop()
    print(min_stack.top())      # Returns 0
    print(min_stack.getMin())   # Returns -2