def countprimes(n):
    primes=[True]*n
    count=0
    for i in range(2,n):
        if primes[i]:
            count+=1
            for j in range(i*i,n,i):
                primes[j] = False
    return count



n=100
print(countprimes(n))
