def minElement(a):
    l,r = 0, len(a)-1
    while(l<r):
        mid = l+(r-l)//2
        
        if(a[mid]>a[r]):
            l = mid+1

        elif(a[mid]<a[r]):
            r = mid
        # else:
        #     r = r-1
    return a[r]


print(minElement([0,1,2,3,4,5]))
print(minElement([11,13,14,17]))
print(minElement([4,5,6,7,8,0,1,2,3]))
print(minElement([7,8,1,2,3,4,5,6]))
print(minElement([3,4,5,1,2]))