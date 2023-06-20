def search_in_rotatelist(list,n):
    l=0
    h=len(list)-1
    while l<=h:
        mid=(l+h)//2
        if list[mid]==n:
            return mid
        elif list[mid]>list[l]:
            if list[mid]>n>=list[l]:
                h=mid-1
            else:
                l=mid+1
        else:
            if list[mid]<n<=list[h]:
                l=mid+1
            else:
                h=mid-1
    return -1

list=[4,5,6,7,0,1,2]
n=7
print(search_in_rotatelist(list,n))