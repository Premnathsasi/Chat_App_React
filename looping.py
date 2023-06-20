
#Armstrong number
a=153
sum=0
temp=a
while temp!=0:
    digit=temp%10
    sum+=digit**3
    temp//=10

if a==sum:
    print('True')
else:
    print('False')

#print digit

a=123
while a>0:
    print(a%10)
    a//=10

#reverse digit
a=1234
rev=0
while a>0:
    dig=a%10
    rev=rev*10+dig
    a//=10
print(rev)

a=1234
print(str(a)[::-1])

#print series
n=10
for i in range(1,n+1):
    if (i**2>n*n):
        break
    print(i**2)


#pattern printing
n=5
for i in range(n):
    for j in range(i,n):
        print('*',end='')

    print()  
n=5
for i in range(n):
    for j in range(i+1):
        print('*',end='')
        
    print()    

n=5
for i in range(n):
    for j in range(i+1):
        print('*',end='')
    for j in range(i,n-1):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')                
    print()   

n=5
for i in range(n-1):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')  
    for j in range(i):
        print('*',end=' ')       
    print()
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n-1):
        print('*',end=' ')  
    for j in range(i,n):
        print('*',end=' ')       
    print()    


#pattern printing using while loop;

n=5
i=1
while i<=n:
    j=n
    while j>=i:
        print('*',end='')
        j-=1
    print()
    i+=1    
n=5
i=1    
while i<=n:
    j=1
    while j<=i:
        print('*',end='') 
        j+=1
    print()
    i+=1       
