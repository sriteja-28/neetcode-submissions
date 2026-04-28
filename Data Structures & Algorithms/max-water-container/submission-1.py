class Solution:
    def maxArea(self, height):
        # initializing two pointers
        left = 0
        right = len(height) - 1
        # storing maximum area
        max_area = 0
        while left < right:
            # computing width
            width = right - left
            # computing height
            h = min(height[left], height[right])
            # updating max area
            max_area = max(max_area, width * h)
            # moving the smaller pointer
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
