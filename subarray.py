a=[1,2,3,4,5]
i=0
while i<len(a):
    j=i
    while j<len(a):
        k=i
        while k<=j:
            print(a[k],end="")
            k+=1
        print()    
        j+=1
        
    i+=1        
    

a=[1,2,3,4,5]
n=len(a)
for i in range(n):
    for j in range(i+1,n+1):
        for k in range(i,j):
            print(a[k],end="")
            
        print()    

            

     