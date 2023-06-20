def prime_no(n):
    primes=[]
    a=2
    while len(primes)<n:
        for j in range(2,a):
            if a%j==0:
                break
        else:
            primes.append(a)
        a+=1
    print(primes)          

                                 
def main():
    n=int(input())
    prime_no(n)
    print(prime_no)
main()                        