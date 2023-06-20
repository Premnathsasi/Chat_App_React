def jewinstone(jewel,stone):
    j=len(jewel)
    s=len(stone)
    count=0
    for a in range(j):
        for b in range(s):
            if jewel[a]==stone[b]:
                count+=1
    return count

jewel='aA'
stone='aAAbbbb' 
print(jewinstone(jewel,stone))