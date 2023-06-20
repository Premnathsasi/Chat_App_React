def lucky_integer(list):
    dict={}
    ans=-1
    for i in range(len(list)):
        dict[list[i]]= dict.get(list[i],0)+1

    for key,value in dict.items():
        if key==value:
            ans=max(ans,key)
    return ans

list=[1,2,2,3,3,3,4,4,4,4]
print(lucky_integer(list))