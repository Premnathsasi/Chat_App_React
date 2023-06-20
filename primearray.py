def prime_no(n):
    primes=[]
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            primes.append(i)
    print(primes)


                 
def main():
    n=int(input())
    prime_no(n)
    print(prime_no)
main()                        