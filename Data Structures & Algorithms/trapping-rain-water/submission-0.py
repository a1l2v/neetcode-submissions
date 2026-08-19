class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0]*len(height)
        for i in range(1,len(height)):
            left_max[i] = max(left_max[i-1],height[i-1])

        right_max = [0]*len(height)
        for i in range(len(height)-2,-1,-1):
            right_max[i] = max(right_max[i+1],height[i+1])

        water_level = [0]*len(height)
        for i in range(len(height)):
            water_level[i] = min(left_max[i],right_max[i])

        for i in range(len(height)):
            if water_level[i]>=height[i]:
                water_level[i] = water_level[i]-height[i]
            else:
                water_level[i] = 0

        return sum(water_level)