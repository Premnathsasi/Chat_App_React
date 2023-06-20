   
def insertsort(a):
    for i in range(1,len(a)):
        j=i
        while a[j] < a[j-1] and j>0:
            a[j-1],a[j]=a[j],a[j-1]
            j-=1

a=[2,4,6,1,3,5]
insertsort(a)
print(a)                

      