pos=-1

def search(arr,n):
    for i in range(len(arr)):
        if arr[i]==n:
            globals()['pos']=i
            return True
    return False

arr=[3,6,1,4,8,9,2]
n=10

if search(arr,n):
    print('Found at',pos)
else:
    print('Not found')

def linearSearch(arr,n):
    for i in range(len(arr)):
        if arr[i]==n:
            return i
    return -1

arr =[2,4,7,8,9,6,5]
n=8
result = linearSearch(arr,n)
if (result ==-1):
    print('Not Found')
else:
    print("Found at",result)