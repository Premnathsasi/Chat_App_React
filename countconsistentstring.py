def countConsistentString(allowed,words):
    count=0
    allowed=set(allowed)
    
    for word in words:
        for letter in word:
            if letter not in allowed:
                count+=1
                break
    return len(words) - count

allowed='ab'
words=['ad','bd','aaab','baa','badab']
print(countConsistentString(allowed,words))