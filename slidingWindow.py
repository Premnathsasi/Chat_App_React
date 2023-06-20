from typing import List
from collections import deque
def maxSlidingWindow(nums,k):
    window = deque()
    res=[]
    for i in range(len(nums)):
        while window and window[0] <= i-k:
            window.popleft()
        while window and nums[window[-1]] < nums[i]:
            window.pop()
        window.append(i)

        if i >= k-1:
            res.append(nums[window[0]])
    return res
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(maxSlidingWindow(nums,k))