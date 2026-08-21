

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while(left <= right):
            mid =(left+right)//2

            if nums[mid] == target:
                return mid

            # including mid, Divide the array into halfs
            # 1) left half - [l:mid+1]
            # 2) right half - [mid:r+1]
            # nums[mid] is lesser than the nums[right] that mean the right portion is sorted
            if nums[mid] < nums[right]:
              # target is greater than the num[mid] and target < nums[right] than, target lies in right only
              # target lies inside that sorted half
              # search in this half
              if nums[mid] < target and target <= nums[right]:
                left = mid + 1
              # search in this other half
              else:
                right = mid - 1
            # nums[mid] is greater than the nums[right] that means the left portion is sorted
            else:
              # target is greater than the num[mid] and target > nums[right] than, target lies in left only
              # target lies inside that sorted half
              # search in this half
              if nums[mid] > target and target >= nums[left]:
                right = mid - 1
              # search in this other half
              else:
                 left = mid + 1
        return -1


sol = Solution()

nums = [3,4,5,6,1,2]
target = 1
print(sol.search(nums,target))