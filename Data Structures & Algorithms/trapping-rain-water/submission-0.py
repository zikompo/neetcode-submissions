class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0 

        water = 0
        l, r = 0, len(height)-1
        leftMax = height[l]
        rightMax = height[r]
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(height[l], leftMax)
                water += leftMax-height[l]         
            else:
                r -= 1
                rightMax = max(height[r], rightMax)
                water += rightMax-height[r]
                
        return water
