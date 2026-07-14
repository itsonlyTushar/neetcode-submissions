class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        n = len(height)

        leftMax = []
        rightMax = [0] * n

        current_max = 0 
        for num in height:
            current_max = max(current_max, num)
            leftMax.append(current_max)

        current_max = 0 
        for i in range(n - 1, -1, -1):
            current_max = max(current_max, height[i])
            rightMax[i] = current_max
    
        for i in range(n):
            h = min(leftMax[i], rightMax[i]) - height[i]
            total += h
        return total