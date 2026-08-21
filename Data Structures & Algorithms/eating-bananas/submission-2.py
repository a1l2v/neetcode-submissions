class Solution:
    def possible(self,piles: List[int],rate: int,h: int) -> bool:
        x = [math.ceil(pile/rate) for pile in piles]

        hours_req = sum(x)
        if hours_req>h:
            return False
        else:
            return True
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        def possible(rate):
            x = [math.ceil(pile/rate) for pile in piles]
            return False if sum(x) > h else True

        while(left<right):
            mid = (left+right)//2

            if possible(mid):
                right = mid
            else:
                left = mid + 1

        return left