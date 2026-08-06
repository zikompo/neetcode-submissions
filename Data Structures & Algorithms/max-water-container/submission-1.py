class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        product = 0
        while l < r:
            mini_product = (r-l) * min(heights[r], heights[l])
            product = max(product, mini_product)
            if heights[r]<heights[l]:
                r -= 1
            elif heights[l]<heights[r]:
                l += 1
            else:
                l, r = l+1, r-1
        return product