def searchMatrix(matrix,target):
    rows = len(matrix)
    cols=len(matrix[0])
    row=0
    col = cols -1
    while row < rows and  col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row+=1
        else:
            col-=1
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix,target))


def nextGreatest(arr, n):  
    max_right=arr[-1]
    arr[-1] = -1
    for i in range(n-2,-1,-1):
        temp = arr[i]
        arr[i] = max_right
        max_right = max(temp, max_right)
	    
    return arr

arr=[16, 17, 4, 3, 5, 2]
n=6
print(nextGreatest(arr,n))


