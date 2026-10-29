class MinStack:

    # Note: Do not use list.insert(idx, val) or list.pop(0) as 
    # these are not O(1) operations

    def __init__(self):

        # tracks all elems added
        self.stack = []

        # tracks the current min of the stack
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        """
        Track the curr minimum in the min stack

        We must use >= since it is likely that we can
        have the same min val in incoming elements
        """
        if self.min_stack == [] or self.min_stack[-1] >= val:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        pop_val = self.top()

        # Popping the last elem is O(1)
        self.stack.pop(-1)
        if pop_val == self.min_stack[-1]:
            self.min_stack.pop(-1)
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
