
def closestPair(a1,a2,t):
    m,n = len(a1),len(a2)
    l,r=0,n-1
    res_l,res_r =0,0
    diff = 100000000000
    while(l<m and r>=0):
        if(abs(a1[l]+a2[r]-t) <= diff):
            res_l = l
            res_r = r
            diff = abs(a1[l]+a2[r]-t)
    
        if(a1[l]+a2[r]<t):
            l+=1
        
        else:
            r-=1
        print(diff)
    return [a1[res_l], a2[res_r]]


a = [1,4,5,9]
b = [10,20,30,40]
t = 19
print(closestPair(a,b,t))