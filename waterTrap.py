def trap(height):
    l=0
    r=len(height)-1
    l_max=r_max=water=0
    while l <= r:
        if height[l] <= height[r]:
            if height[l] > l_max:
                l_max = height[l]
            else:
                water+=l_max - height[l]
            l+=1
        else:
            if height[r] > r_max:
                r_max = height[r]
            else:
                water+=r_max - height[r]
            r-=1
    return water

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))