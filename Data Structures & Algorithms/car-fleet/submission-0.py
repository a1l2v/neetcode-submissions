class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = list(zip(position,speed))
        combined.sort(key=lambda x:x[0])


        stack = []
        stack.append(combined[0])

        for i in range(1,len(combined)):
            pos,speed = combined[i]
            while(len(stack)>0  and speed < stack[-1][1]):
                relative_speed = stack[-1][1]-speed
                time = (pos - stack[-1][0])/relative_speed
                meet = pos + time * speed
                if meet>target:
                    break
                else:
                    stack.pop()

            stack.append((pos,speed))

        return len(stack)