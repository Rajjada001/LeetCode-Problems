# https://leetcode.com/problems/find-in-mountain-array/


def peakIndexMountainArray(a):
    l,h=0,len(a)-1
    while(l<h):
        mid = l+(h-l)//2
        if(a[mid]>a[mid+1]):
            h = mid
        else:
            l = mid+1
    return l

