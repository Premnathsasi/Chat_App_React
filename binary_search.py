pos=-1
def binary_search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False

list=[1,3,5,7,9]
n=5
if binary_search(list,n):
    print('Found at',pos)
else:
    print('Not found')

    
# Iterative form
def binary(list,n):
    low=0
    high=len(list)-1
    mid=0

    while low<=high:
        mid=(low+high)//2

        if list[mid]<n:
            low=mid+1
        elif list[mid]>n:
            high=mid-1
        else:
            return mid
    return -1

list=[1,3,5,7,9]
n=5
result=binary(list,n) 
if result !=-1:
    print('Present',str(result))
else:
    print('Not present')

#recursive
def binary_search(list,low,high,n):
    if low<=high:
        mid=(low+high)//2

        if list[mid]==n:
            return mid
        elif list[mid]<n:
            return binary_search(list,mid+1,high,n)
        else:
            return binary_search(list,low,mid-1,n)
    return -1

list=[1,3,5,7,9]
n=5
result=binary_search(list,0,len(list)-1,n)
if result!= -1:
    print('Presented at',str(result))
else:
    print('Not Presented')
