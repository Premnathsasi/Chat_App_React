
def mergesort(nums):
    if len(nums)>1:
        left_arr=nums[:len(nums)//2]
        right_arr=nums[len(nums)//2:]

        mergesort(left_arr)
        mergesort(right_arr)

        i=0
        j=0
        k=0
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<right_arr[j]:
                nums[k]=left_arr[i]
                i+=1
            else:
                nums[k]=right_arr[j]
                j+=1
            k+=1

        while i<len(left_arr):
            nums[k]=left_arr[i]
            i+=1
            k+=1
        while j<len(right_arr):
            nums[k]=right_arr[j]
            j+=1
            k+=1

n=[3,6,1,7,2,4,9]
mergesort(n)
print(n)

def merge(nums1, m,nums2, n):
    i=m-1
    j=n-1
    k= m+n-1
    while j >=0:
        if i >=0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i-=1
        else:
            nums1[k] = nums2[j]
            j-=1
            
        k-=1
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1,m,nums2,n)
print(nums1)