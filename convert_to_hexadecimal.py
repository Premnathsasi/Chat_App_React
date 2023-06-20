def tohex(num):
    if num ==0: return '0'
    mp='0123456789abcdef'
    ans=''
    for i in range(8):
        ans=mp[num%16] + ans
        num=num//16
    return ans.lstrip('0')

def main():
    n=int(input())
    print (tohex(n))
main()