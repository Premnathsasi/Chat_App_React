class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = bin(n)[2:]
        for i in range(1,len(n)):
            if n[i]==n[i-1]:
                return False
        return True
#solution 2
# return '00' not in n and '11' not in n

def main():
    n=int(input())
    s=Solution()
    output = s.hasAlternatingBits(n)
    if(output):
        print("true")
    else:
        print("false")
    
main()