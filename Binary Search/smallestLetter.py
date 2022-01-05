
import time
start = time.time()


def floor(a,t):
    l,h=0,len(a)-1
    while(l<=h):
        mid = l+(h-l)//2

        if(a[mid]>t):
            h = mid-1
        else:
            l = mid+1
            
    return a[l%len(a)]
    

t = int(input("Enter T:"))
for _ in range(t):
    t = input("Enter n:")
    a = list(map(str, input().rstrip().split()))
    print(floor(a,t))
    print("It took %s milli seconds"%((time.time()-start)*10))
