import time
start = time.time()


def InFiniteArray(a,t):
    s,e = 0,1
    # condition for the target to lie in the range
    while(t > a[e]):
        newStart = e + 1
        # double the end
        # previous end + size of the box
        e = e + (e-s+1)*2
        s = newStart
    return BinarySearch(a,t,s,e)

def BinarySearch(a,t, l,h):
    while(l<=h):
        mid = l+(h-l)//2

        if(a[mid]>t):
            h = mid-1
        elif(a[mid]<t):
            l = mid+1
        else:
            return mid
    return -1
    

t = int(input("Enter T:"))
for _ in range(t):
    n = int(input("Enter n:"))
    a = list(map(int, input().rstrip().split()))
    print(InFiniteArray(a,n))
    print("It took %s milli seconds"%((time.time()-start)*100))
