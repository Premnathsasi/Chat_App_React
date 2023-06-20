a=[-1,-100,3,99]
k=2
a[:] = a[-k:] + a[:-k]
print(a)

a=[-1,-100,3,99]
k=2
for i in range(0,k):
    aa=a.pop()
    a.insert(0,aa)
print(a)