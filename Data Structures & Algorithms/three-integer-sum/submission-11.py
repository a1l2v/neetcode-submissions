class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)-2):

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
                    if solution not in ans:
                        ans.append(solution)

                    left += 1
                    right -= 1
        
        return ans

        