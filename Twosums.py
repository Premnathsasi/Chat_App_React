def twosums(nums,target):
    dict={}
    for i,j in enumerate(nums):
        dif= target - j
        if dif in dict:
            return [dict[dif],i]
        dict[j]=i 


nums=[2,7,11,15]
target=13
print(twosums(nums,target))