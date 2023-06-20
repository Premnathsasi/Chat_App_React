# #factorial
def fact(n):
    if n==0:
        return 1
    else:
        return(n*fact(n-1))

r=fact(5)
print(r)
# # find sum
# def fsum(n):
#     if n==1:
#         return 1
#     return n+fsum(n-1)

# s=fsum(5)
# print(s)

# #fibonacci series
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)

if __name__=='__main__':
    print(fib(6))



# #multiples
# def multi(num,i):
#     if i <=10:
#         print(num,'x',i,'=',num*i)
#         multi(num,i+1)
# multi(5,1)

# #permutation
# def permutation(string):
#     if len(string)==1:
#         return [string]
#     a=[]
#     for i in string:
#         for j in permutation(string.replace(i,'')):
#             a.append(i+j)
#     return (a)

# print(permutation('ABC'))

# #sub sequence
# def subsequence(arr,index,subarr):
#     if index==len(arr):
#         if len(subarr)!=0:
#             print (subarr)
#     else:
#         subsequence(arr,index+1,subarr)
#         subsequence(arr,index+1,subarr+[arr[index]])
#     return
# arr=[1,2,3]
# subsequence(arr,0,[])
