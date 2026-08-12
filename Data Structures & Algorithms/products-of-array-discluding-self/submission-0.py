class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftProd = [0]*n
        leftProd[0] = 1
        for i in range(1,n):
            leftProd[i] = leftProd[i-1]*nums[i-1]
        rightProd = [0]*n
        rightProd[n-1] = 1
        for i in range(n-2,-1,-1):
            rightProd[i] = rightProd[i+1]*nums[i+1]
        
        res = []
        for i in range(n):
            res.append(leftProd[i]*rightProd[i])
        return res