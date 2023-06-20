n=20
def is_sharpees(num):
  sum=0
  for i in str(num):
    sum+=int(i)
  if sum % 5==0:
    return sum

def sharpee_number(n):
  sh=[]
  num=1
  while len(sh) < n:
    if is_sharpees(num):
      sh.append(num)
    num+=1
  return sh

print(sharpee_number(n))


def rotate( arr, n):
    # arr[:] = arr[-1:] + arr[:-1]
    temp=arr[-1]
    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0]=temp
    return arr

arr=[1, 2, 3, 4, 5]
n=5
print(rotate(arr,n))