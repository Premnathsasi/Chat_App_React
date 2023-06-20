   
def selectsort(a):
    for i in range(len(a)):
        minpos=i
        for j in range(i,len(a)):
            if a[j]<a[minpos]:
                minpos=j
        a[i],a[minpos]=a[minpos],a[i]  
  

a=[2,4,6,1,3,5]
selectsort(a)
print(a)                

      