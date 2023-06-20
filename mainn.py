# def bigg(arr):
#     temp=[n for n in arr]
#     temp.sort(reverse=True)
#     dict={}
#     for i,n in enumerate(temp):
#         if n not in dict:
#             dict[n]=i
#     return [dict[n] for n in arr]

# arr=[10,12,6,4,16,1]
# print(bigg(arr))


# def dup(a,t):
#     dict={}
#     for num in a:
#         if num not in dict:
#             dict[num]=0
#         dict[num]+=1

#     for i,j in dict.items():
#         if j>t:
#             return True
#     return False

# a=[9,5,3,2,1,5,1,4,3,5,4,6,5]
# t=6
# print(dup(a,t))

# arr = ['a','b','c','d','e']

# for i in range(len(arr)):
#     for j in range(len(arr)):
#         print(arr[i], arr[j])
# n=10
# a=2
# arr=[]
# while len(arr)< n:
#     for j in range(2,a):
#         if a%j == 0:
#             break
#     else:
#         arr.append(a)
#     a+=1
# print(arr)

# arr1 = ['a','b','c','d','e']
# arr2= ['z','x','m','a']

# def fun(a1, a2):
#     a = set(a1)
#     b = set(a2)
#     if (a & b):
#         return True
#     return False
            
# print(fun(arr1,arr2))

# def reverse(a):
#     str =''
#     for i in range(len(a)-1,-1,-1):
#         str+=a[i]
#     return str
# print(reverse('premnath'))
# print('premnath'[::-1])

# def shuffle(nums,n):
#     ar=[]
#     for i in range(n):
#         ar.append(nums[i])
#         ar.append(nums[i+n])
#     return ar
# nums = [2,5,1,3,4,7]
# n = 3
# print(shuffle(nums,n))

# nums = [8,1,2,2,3]
# max_sort = sorted(nums)
# print(max_sort)
# print(max_sort.index(3))
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# arr = []
# for i in range(len(matrix)):
#     list_col = []
#     for j in range(len(matrix)):
#         list_col.append(matrix[j][i])
#     arr.append(list_col)
# print(arr)

# sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# ans=0
# for i in sentences:
#     ans = max(ans, i.count(' ')+1)
# print(ans)

# arr=[[1,2,3],[4,5,6]]
# for i in range(len(arr[0])):
#     for j in range(len(arr)):
#         print(arr[j][i])

# def search(nums, target):
#     l=0
#     r=len(nums)-1
#     while l <=r:
#         mid=(l+r)//2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] >= nums[l]:
#             if target >= nums[l] and target < nums[mid]:
#                 r = mid -1
#             else:
#                 l = mid + 1
#         else:
#             if target <= nums[r] and target > nums[mid]:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#     return -1
# nums = [4,5,6,7,0,1,2]
# target = 5
# print(search(nums,target))
#

# # min dif sum
# def findMinDiff(arr, n, m):
#     if (m == 0 or n == 0):
#         return 0
 
#     arr.sort()

#     if (n < m):
#         return -1
 
#     min_diff = arr[n-1] - arr[0]
 
#     for i in range(len(arr) - m + 1):
#         min_diff = min(min_diff,  arr[i + m - 1] - arr[i])
 
#     return min_diff
    
# if __name__ == "__main__":
#     arr = [12, 4, 7, 9, 2, 23, 25, 41,
#            30, 40, 28, 42, 30, 44, 48,
#            43, 50]
#     m = 7  # Number of students
#     n = len(arr)
#     print("Minimum difference is", findMinDiff(arr, n, m))

# reverse a word
# s = "the sky is blue"
# def reverseWords(s):
#         # x = s.split()
#         # return ' '.join(x[::-1])
#     res = []
#     temp=''
#     for i in s:
#         if i != ' ':
#             temp+=i
#         elif temp != '':
#             res.append(temp)
#             temp=''
#     if temp != '':
#         res.append(temp)
#     return (' '.join(res[::-1]))

# print(reverseWords(s))

# def removeConsecutiveCharacter(S):
#         # code here
#     stack = []
#     arr = list(S)
#     for i in range(len(arr)):
#         if len(stack) == 0:
#             stack.append(arr[i])
#         else:
#             if arr[i] == stack[-1]:
#                 pass
#             else:
#                 stack.append(arr[i])
#     return ''.join(stack)
# S = "aabb"
# print(removeConsecutiveCharacter(S))

#
# allowed = "ab"
# words = ["ad","bd","aaab","baa","badab"]
# count=0
# for i in words:
#     for j in i:
#         if j not in allowed:
#             count+=1
# print(len(words) - count)

#Longest Common Prefix

# def long(v):
#     ans=""
#     v=sorted(v)
#     first=v[0]
#     last=v[-1]
#     for i in range(min(len(first),len(last))):
#         if(first[i]!=last[i]):
#             return ans
#         ans+=first[i]
#     return ans
# strs = ["flower","flow","flight"]
# print(long(strs))

# Valid Parentheses

# s = "()[{}"
# def isValid(s):
#     st=[]
#     d={']':'[','}':'{',')':'('}
#     for char in s:
#         if char in d.values():
#             st.append(char)
#         elif char in d.keys():
#             if st==[] or d[char]!=st.pop():
#                 return False
#         else:
#             return False
#     return st==[]

# print(isValid(s))

# nums = [1,3,5,6]
# target = 2
# def searchInsert(nums,target):
#     l=0
#     r=len(nums)-1
#     while l <= r:
#         mid = (l+r)//2
#         if nums[mid] == target:
#             return mid
#         elif target < nums[mid]:
#             r = mid -1
#         else:
#             l = mid + 1
#     return l
# print(searchInsert(nums,target))

def subarraySum(nums,k):
    dict = {0: 1}
    count = 0
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        if sum - k in dict:
            count+=dict[sum-k]
        if sum in dict:
            dict[sum]+=1
        else:
            dict[sum] = 1

    return count
nums = [1,1,1]
k = 2
print(subarraySum(nums,k))

# def searchRange(nums,target):
#     l=0
#     r=len(nums)-1
#     s=-1
#     while l <= r:
#         mid = (l+r)//2
#         if nums[mid] >= target:
#             r = mid -1
#         else:
#             l = mid +1
#         if nums[mid] == target:
#             s=mid
#     if s == -1:
#         return [-1,-1]

#     l=0
#     r=len(nums)-1
#     e=-1
#     while l <= r:
#         mid= (l+r)//2
#         if nums[mid] <= target:
#             l = mid +1
#         else:
#             r = mid -1
#         if nums[mid] == target:
#             e = mid
#     return [s,e] 
# nums = [5,7,7,8,8,10] 
# target = 8
# print(searchRange(nums,target))
# arr=[[1,5],[7,3],[3,5]]
# s =0
# max_=0
# for i in arr:
#   s=max(i)
#   if s > max_:
#     max_ = s
# print(max_)


# #jump Game
# def canJump(nums):
#     max_index = 0
#     for i, jump in enumerate(nums):
#         if i > max_index:
#             return False
#         max_index = max(max_index, i+jump)
        
#     return True
# nums = [3,2,1,1,4]
# print(canJump(nums))

# #jump Game 2
# def jump(nums):
#     n = len(nums)
#     if n == 1:
#         return 0
        
#     jumps = 0
#     cur_end = 0
#     cur_max_reach = 0
    
#     for i in range(n-1):
#         cur_max_reach = max(cur_max_reach, i + nums[i])
#         if i == cur_end:
#             jumps += 1
#             cur_end = cur_max_reach
#             if cur_max_reach >= n-1:
#                 break
    
#     return jumps
# nums = [2,3,1,1,4]
# print(jump(nums))


arr = ["vaibhav", "almanac", "is", "fat", "button", "aabaca"]
def sort_(arr):
  def sort_func(arr):
    return arr.count('a'), len(arr)
  arr.sort(key=sort_func,reverse=True)
  return arr
  
print(sort_(arr))

# def r(i):
#   if i ==6:
#     return
#   else:
#     print(i)
#     r(i+1)
    
# r(1)

# def print_multiples_of_5(num):
#     if num >= 5:
#         print(num)
#         print_multiples_of_5(num - 5)
        
        
# print_multiples_of_5(25)

# def sum(x):
#   if x==1: return 1
#   else:
#     return x + sum(x-1)

# print(sum(5))


# def sum_digits(n): 
#   if n <= 9: 
#     return n 
#   last_digit = n % 10 
#   return sum_digits(n // 10) + last_digit

# print(sum_digits(552)) #returns 12


def permutation(n):

    if len(n)==1:

        return [n]

    a=[]

    for i in n:

        for j in permutation(n.replace(i,'')):

            a.append(i+j)

    return (a)



print(permutation('abc'))