class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)-2):

            if(i>0 and nums[i]==nums[i-1]):
                continue
            first = nums[i]
            target = -first

            left = i+1
            right = len(nums)-1

            while(left<right):

                sum = nums[left] + nums[right]

                if sum > target:
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    solution = [first,nums[left],nums[right]]
                    ans.append(solution)
                    left += 1
                    right -= 1
                    while(left<right and nums[left]==nums[left-1]):
                        left += 1
                    while(left<right and nums[right]==nums[right+1]):
                        right -= 1
        
        return ans

        