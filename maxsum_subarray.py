a=[5,2,-4,-5,3,-1,2,3,1]
max_s=a[0]
i=0
while i<len(a):
    j=i
    while j<len(a):
        k=i
        sum=0
        while k<=j:
            sum=sum+a[k]

            k+=1
        if sum>max_s:
            max_s=sum    
        j+=1
        
    i+=1        
print(max_s)   


a=[5,2,-4,-5,3,-1,2,3,1]
max_s=a[0]
n=len(a)
for i in range(n):
    sum=0
    for j in range(i,n):
        sum=sum+a[j]
        if sum>max_s:
            max_s=sum    

print(max_s)   