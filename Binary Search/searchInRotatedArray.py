def searchInRotatedSortedArray(a,t):
    l,r = 0,len(a)-1

    while(l<=r):
        mid = l+(r-l)//2

        if(a[mid]==t):
            return mid
        # search left sorted array
        elif(a[l]<= a[mid]):
            if( t > a[mid] or t< a[l]):
                l = mid+1
            else:
                r = mid-1

        # search right sorted array
        else:
            if(t < a[mid] or t > a[r]):
                r = mid-1
            else:
                l = mid+1
    
    return -1


print(searchInRotatedSortedArray([5,6,7,8,9,10,0,1,2,3],10))
print(searchInRotatedSortedArray([7,8,0,1,2,3,4,5,6],5))