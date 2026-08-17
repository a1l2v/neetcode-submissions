class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        corres = {'(':')','[':']','{':'}'}
        for i in range(len(s)):
            if s[i] in ['(','{','[']:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                curr = stack.pop()
                if corres[curr] != s[i]:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False
