class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        if n == 1:
            return 1
        if n == 0:
            return 0
        count,maxV = 1,1
        for i in range(n-1):
            if nums[i+1]-nums[i]==1:
                count += 1
            elif nums[i+1] - nums[i]==0:
                maxV = max(maxV, count)
            else:
                count = 1
            
            maxV = max(maxV, count)
        return maxV