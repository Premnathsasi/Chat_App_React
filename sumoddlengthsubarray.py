a=[1,4,2,5,3]
n=len(a)
s=0
for i in range(n):
    for j in range(i,n,2):
        s=s+sum(a[i:j+1])

print(s)    