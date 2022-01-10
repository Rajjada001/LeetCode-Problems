def twoSumSortedArray(a,t):
    i,j=0,len(a)-1
    while(i<j):
        if(a[i]+a[j]==t):
            return [a[i],a[j]]
        elif(a[i]+a[j]<t):
            i += 1

        else:
            j -= 1


print(twoSumSortedArray([2,3,4,5,8,9,10,11],17))