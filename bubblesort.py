   
def bubblesort(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

a=[3,6,7,2,1,9]
bubblesort(a)
print(a)                

