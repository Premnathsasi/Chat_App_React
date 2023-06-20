def greater(nums):
  n = len(nums)
  result = [-1] * n
  stack = []

  for i in range(2 * n):
    j = i % n

    while stack and nums[j] > nums[stack[-1]]:
      top = stack.pop()
      result[top] = nums[j]
    stack.append(j)

  return result
nums = [1,2,1]
print(greater(nums))  