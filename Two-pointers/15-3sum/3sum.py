class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while j<k:
                temp = nums[i]+nums[j]+nums[k]
                if temp==0:
                    res.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif temp<0:
                    j+=1
                else:
                    k-=1
        return list(res)