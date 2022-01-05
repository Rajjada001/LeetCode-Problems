import time
start = time.time()


def squareRoot(n):
    l,h=0,n-1
    while(l<h):
        mid = l+(h-l)//2
        if(mid*mid > n):
            h = mid-1
        elif(mid*mid<n):
            l = mid+1
        
        else:
            return mid
    return l

t = int(input("Enter T:"))
for _ in range(t):
    n = int(input("Enter n:"))
    print(squareRoot(n))
    print("It took %s milli seconds"%((time.time()-start)*100))
