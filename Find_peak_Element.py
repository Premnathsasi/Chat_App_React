def findpeakElement(nums):
    l=0
    h=len(nums)-1
    if len(nums)==1:
        return 0
    while l<=h:
        mid=(l+h)//2
        if nums[mid] >nums[mid+1] and nums[mid]>nums[mid-1]:
            return mid
        elif nums[mid]<nums[mid+1]:
            l=mid+1
        else:
            h=mid-1
    return h if nums[h]>nums[mid] else mid

list=[1,2]
print(findpeakElement(list))

