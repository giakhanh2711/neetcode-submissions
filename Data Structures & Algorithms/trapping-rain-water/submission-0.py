class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft, maxright = [0] * len(height), [0] * len(height)
        n = len(height)
        for i in range(1, len(height)):
            maxleft[i] = max(maxleft[i - 1], height[i - 1])
            maxright[n - i - 1] = max(maxright[n - i], height[n - i])
        
        water = 0
        for i in range(len(height)):
            water += max(0, min(maxleft[i], maxright[i]) - height[i])
        
        return water