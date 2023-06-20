class solution:
    def countsetbit(self,n):
        ans=0
        while n:
            n=n & (n-1)
            ans+=1
        return ans
        # solution 2
        # return bin(n).count('1')

def main():
    n=int(input())
    s=solution()
    output=s.countsetbit(n)
    print(output)
