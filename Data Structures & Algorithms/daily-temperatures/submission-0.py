class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        stack.append((temperatures[0],0))

        for i in range(1,len(temperatures)):
          while(len(stack)>0 and temperatures[i]>stack[-1][0]):
            temp,idx = stack.pop()
            result[idx] = i-idx
          stack.append((temperatures[i],i))


        return result
            
