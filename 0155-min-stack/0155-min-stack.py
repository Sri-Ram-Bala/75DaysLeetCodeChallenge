class MinStack:

    def __init__(self):
        # The main stack stores all elements
        self.stack = []
        # The min_stack stores the minimum at each state of the main stack
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        # If min_stack is empty, the current val is the minimum.
        # Otherwise, compare val with the current top of min_stack.
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            current_min = min(val, self.min_stack[-1])
            self.min_stack.append(current_min)

    def pop(self) -> None:
        # Both stacks must stay in sync
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]