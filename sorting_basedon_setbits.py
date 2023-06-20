a=[7,6,4,3,9,2]
b=[]
for i in range(len(a)):
    count=0
    for j in range(32):
        bit=(a[i]>>j) & 1
        if bit==1:
            count+=1
    b.append(count)

for i in range(len(a)-1,0,-1):
    for j in range(i):
        if b[j]>b[j+1] or b[j]==b[j+1] and a[j]>a[j+1]:
            b[j],b[j+1]=b[j+1],b[j]
            a[j],a[j+1]=a[j+1],a[j]

for i in range(len(a)):
    print(a[i],'-->',b[i])
