# https://leetcode.com/problems/peak-index-in-a-mountain-array/


import time
start = time.time()


def peakIndexMountainArray(a):
    l,h=0,len(a)-1
    while(l<h):
        mid = l+(h-l)//2
        if(a[mid]>a[mid+1]):
            h = mid
        else:
            l = mid+1
    return l


print(peakIndexMountainArray([1,2,4,5,3,2,1])) # index:3
print(peakIndexMountainArray([12,51,42,7])) #index:1
print(peakIndexMountainArray([1,2,65,87,98,118,97,85,63,1])) #index:5


print("It took %s milli seconds"%((time.time()-start)*1000))
