a=[[1,2,3],[5,3],[5,6]]
n=len(a)
max=0
for i in range(n):
    sum=0
    for j in range(len(a[i])):
        sum=sum+a[i][j]

        if sum>max:
            max=sum
print(max)            