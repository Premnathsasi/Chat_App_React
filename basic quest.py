

n=[1,2,1]
a=[]
for i in range(len(n)*2):
    a.append(n[i%len(n)])
print(a)

n=234
prod=1
sum=0
while n:
    d=n%10
    prod=prod*d
    sum=sum+d
    n//=10
print(prod-sum)

n=5
for i in range(n):
    for j in range(i+1):
        print('*',end='')
    for j in range(i,n-1):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print()

n=7
ans=0
while n>1:
    if n%2!=0:
        ans=ans+n//2
        n=(n//2)+1
    else:
        ans=ans+n/2
        n/=2
print(int(ans))


a=[1,1,1,1]
my_count=0
dic={}
for i in a:
    if i in dic:
        my_count+=dic[i]
        dic[i]+=1

    else:
        dic[i]=1
print(my_count)