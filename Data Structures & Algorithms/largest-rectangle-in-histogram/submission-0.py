class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            new_idx = i
            while stack and h < stack[-1][1]:
                higher = stack.pop()
                new_idx = higher[0]
                area = (i - new_idx) * higher[1]
                maxArea = max(area, maxArea)

            stack.append([new_idx, h])

        for i, h in stack:
            area = (len(heights) - i) * h
            maxArea = max(area, maxArea)
            
        return maxArea     