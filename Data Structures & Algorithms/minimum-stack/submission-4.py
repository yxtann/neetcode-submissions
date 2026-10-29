class MinStack:

    def __init__(self):

        # tracks all elems added
        self.stack = []

        # tracks the current min of the stack
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.insert(0, val)
        if self.min_stack == [] or self.min_stack[0] >= val:
            self.min_stack.insert(0, val)
        

    def pop(self) -> None:
        pop_val = self.top()
        self.stack.pop(0)
        if pop_val == self.min_stack[0]:
            self.min_stack.pop(0)
        

    def top(self) -> int:
        return self.stack[0]
        

    def getMin(self) -> int:
        return self.min_stack[0]
