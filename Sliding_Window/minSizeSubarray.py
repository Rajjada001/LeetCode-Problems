

import sys

def minSizeSubArray(a,t):
    # define pointers
    l = r = 0
    # minimum subarray length and sum
    minVal, currSum = sys.maxsize, 0
    # minVal sub array len
    while(r<len(a)):
        currSum += a[r]

        while(t <= currSum):
            minVal= min(minVal, r-l+1)
            currSum -= a[l]
            l+=1
        r+=1

    
    return minVal if minVal != sys.maxsize else 0
 

print(minSizeSubArray([2,3,1,2,4,3],7))