def searchInRotatedSortedArray(a,t):
    l,r = 0,len(a)-1

    while(l<=r):
        mid = l+(r-l)//2

        if(a[mid]==t):
            return mid
        elif(a[mid]>=a[l]):
            
            if a[mid]>=t and a[l]<=t:
                r = mid-1
            else:
                l = mid+1
        
        else:
            if(a[mid]<=t and a[r]>=t):
                l = mid+1
            else:
                r = mid-1
    
    return -1


print(searchInRotatedSortedArray([4,5,6,7,8,0,1,2,3],3))
print(searchInRotatedSortedArray([7,8,0,1,2,3,4,5,6],5))