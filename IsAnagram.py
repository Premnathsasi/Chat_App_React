# Other solution
# Counter(s)==Counter(t)

def isanagram(s,t):
    if len(s)!=len(t):
        return False
    sdict={}
    tdict={}
    for char in s:
        if char not in sdict:
            sdict[char]=1
        else:
            sdict[char]+=1

    for char in t:
        if char not in tdict:
            tdict[char]=1
        else:
            tdict[char]+=1

    if sdict==tdict:
        return True
    return False


s='anagram'
t='nagaram'
print(isanagram(s,t))


def anagram(s,t):
    if len(s)!=len(t):
        return False
    l='abcdefghijklmnopqrstuvwxyz'
    for char in l:
        if s.count(char)!=t.count(char):
            return False
    return True


s='car'
t='rac'
print(isanagram(s,t))