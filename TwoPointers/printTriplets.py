def printTriplets(a):
    a.sort()
    for i in range(len(a)-1):
        l = i+1
        r = len(a)-1
        while(l<r):
            if(a[i]+a[l]+a[r]==0):
                 print([a[i],a[l],a[r]])
                 l+=1
                 r-=1            
            elif(a[i]+a[l]+a[r] < 0):
                l+=1
            else:
                r-=1
        
        

printTriplets([0,-1,2,-3,1])