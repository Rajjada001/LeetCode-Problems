from turtle import right


def sortedSquares(a):
    n = len(a)
    l,r=0,n-1
    res = [0]*n
    for i in range(n-1,-1,-1):
        if(abs(a[l]) >= abs(a[r])):
            res[i] = a[l]*a[l]
            l += 1
        else:
            res[i] = a[r]*a[r]
            r -= 1

    return res


print(sortedSquares([-9,-5,1,2,5,7,9]))