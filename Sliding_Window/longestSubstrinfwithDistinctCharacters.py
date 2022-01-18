def longestSumWithTwoDistinctCharacters(a):
    
    l = r = maxLen=0
    cMap = {}
    while(r<len(a)):
        cMap[a[r]] = r
        # counter our window if it doesn't satisfy the condition
        if(len(cMap)>2):
            min_index = min(cMap.values())
            l = min_index + 1
            del cMap[a[min_index]]
        maxLen = max(maxLen, r-l+1)
        r+=1

    return maxLen

print(longestSumWithTwoDistinctCharacters("eceba"))
print(longestSumWithTwoDistinctCharacters("eceeeebbbba"))