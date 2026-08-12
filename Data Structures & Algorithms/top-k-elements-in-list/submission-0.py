import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_list = []
        ans = []
        counter = Counter(nums)

        for num,freq in counter.items():
            heapq.heappush(sorted_list,(-freq,num))

        for _ in range(k):
            freq, num = heapq.heappop(sorted_list)
            ans.append(num)

        return ans
