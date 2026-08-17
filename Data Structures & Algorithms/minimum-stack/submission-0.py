class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ele = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_ele is None:
            self.min_ele = val
        else:
            if self.min_ele > val:
                self.min_ele = val
        

    def pop(self) -> None:
        ele = self.stack.pop()
        if len(self.stack) == 0:
            self.min_ele = None
        else:
            if self.min_ele == ele:
                self.min_ele = min(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_ele
