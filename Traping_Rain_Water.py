# Two pointer approach
# given an block of heights and find the how much water trap in those blocks

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

def trapped_water(heights):
    left, right = 0, len(heights)-1
    leftMax, rightMax = heights[left], heights[right]
    res = 0
    while left < right:
        if leftMax < rightMax:
            left += 1
            leftMax = max(leftMax, heights[left])
            res += leftMax - heights[left]
        else:
            right -= 1
            rightMax = max(rightMax,heights[right])
            res += rightMax - heights[right]
    return res

heights = list(map(int,input().split()))
print(trapped_water(heights))