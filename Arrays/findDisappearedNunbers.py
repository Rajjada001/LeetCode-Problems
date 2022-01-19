#https://leetcode.com/explore/featured/card/fun-with-arrays/523/conclusion/3270/

# O(n) space and time complexities
'''
def findDisappearedNums(nums):
        hSet = set()
        n = len(nums)
        for i in range(n):
            hSet.add(nums[i])
        res = []
        
        for i in range(1,len(nums)+1):
            if i not in hSet:
                res.append(i)
        return res
'''

# def findDisappearedNums(nums):
#     pass

# print(findDisappearedNums([4,3,2,7,8,2,3,1])) #[5,6]

t = int(input())
for _ in range(t):
    a,b,c = map(int, input().split())
    print(a+b+c)