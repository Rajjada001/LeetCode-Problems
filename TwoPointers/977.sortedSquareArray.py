def sortedSquareArray(a):
        left,right = 0, len(a)-1
        res = [0]*len(a) 
        i = len(a)-1
        while i >= 0:
            
            if(abs(a[left])>abs(a[right])):
                res[i] = a[left]*a[left]
                left += 1
            
            else:
                print(right)
                res[i] = a[right]*a[right]
                right -= 1
            i -=1
        
        return res


nums = [-7,-3,2,3,11]

print(sortedSquareArray(nums))