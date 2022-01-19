# https://leetcode.com/explore/featured/card/fun-with-arrays/523/conclusion/3228/

def heightChecker(heights):
    
        dup = heights[::]
        dup.sort()
        
        count = 0
        
        for i in range(len(heights)):
            if heights[i] != dup[i]:
                count+=1
            
        return count
        

print(heightChecker([1,1,4,2,1,3]))
print(heightChecker([5,4,3,2,1,2]))