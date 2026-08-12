class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        max_len = 0

        for i in range(len(nums)):
            if (nums[i]+1) in elements:
                continue
            prev = nums[i]
            count = 0
            while(prev in elements):
                count += 1
                prev = prev - 1

            max_len = max(count,max_len)

        return max_len

        