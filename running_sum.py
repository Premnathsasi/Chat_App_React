a=[1,2,3,4,5]
for i in range(1,len(a)):
    a[i]=a[i]+a[i-1]
print(a)
      