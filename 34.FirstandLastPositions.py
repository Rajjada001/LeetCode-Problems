# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

def firstLastPositions(a,target):
        res = [-1,-1]
        n = len(a)
        l,h = 0,n-1
        
        while(l<=h):
            mid = l+(h-l)//2
            if(a[mid]>target):
                h = mid-1
            elif(a[mid]<target):
                l = mid + 1
            
            else:
                res = [mid,mid]
#               check the left side of mid
                while(mid-1 >= 0 and a[mid-1]==target):    
                    mid = mid-1
                    res[0] = mid
                while(mid+1<n and a[mid+1]== target):
                    mid = mid+1
                    res[1] = mid
                break
                
        return res

t = int(input("Enter T:"))
for _ in range(t):
    a = list(map(int, input().rstrip().split()))
    target = int(input("Enter target:"))
    print(firstLastPositions(a,target))