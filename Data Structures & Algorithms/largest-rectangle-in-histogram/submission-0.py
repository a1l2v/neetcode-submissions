class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for idx in range(len(heights)):
            height = heights[idx]
            start = idx

            while stack and height < stack[-1][1]:
                i, h = stack.pop()
                area = (idx - i) * h
                max_area = max(area, max_area)
                start = i

            stack.append((start, height))

        while stack:
            i, h = stack.pop()
            area = (len(heights) - i) * h
            max_area = max(area, max_area)

        return max_area