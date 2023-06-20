def subArray(a):
    i=0
    while i<len(a):
        j=i
        while j<len(a):
            k=i
            while k<=j:
                print(a[k],end='')
                k+=1
            print()
            j+=1
        i+=1
a=[1,2,3]
subArray(a)

def sub(a):
    for i in range(len(a)):
        for j in range(i,len(a)+1):
            for k in range(i,j):
                print(a[k],end='')
            print()
a=[1,2,3]
sub(a)