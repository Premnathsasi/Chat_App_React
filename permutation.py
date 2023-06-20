def permute(nums):
    def backTrack(nums,curper,res):
        if len(curper)==len(nums):
            res.append(curper[:])
        else:
            for num in nums:
                if num not in curper:
                    curper.append(num)
                    backTrack(nums,curper,res)
                    curper.pop()
    res=[]
    backTrack(nums,[],res)
    return res
nums = [1,2,3]
print(permute(nums))