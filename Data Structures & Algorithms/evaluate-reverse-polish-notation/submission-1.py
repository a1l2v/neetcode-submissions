class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] in ["*","/","-","+"]:
                ele2 = int(stack.pop())
                ele1 = int(stack.pop())
                if tokens[i] == "+":    
                    stack.append(ele1 + ele2)
                elif tokens[i] == "-":
                    stack.append(ele1 - ele2)
                elif tokens[i] == "*":
                    stack.append(ele1 * ele2)
                else:
                    stack.append(ele1 / ele2)

            else:
                stack.append(tokens[i])

        return int(stack[0])