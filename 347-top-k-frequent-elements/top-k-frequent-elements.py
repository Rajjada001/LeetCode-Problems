class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # step 1: create a hashmap to store the count of each element
        hm = {}
        # step 2: Create buckets to store elements based on their frequency
        buckets = [[] for i in range(len(nums)+1)]

        #step3: get the counts
        for n in nums:
            hm[n] = 1 + hm.get(n, 0)
        # step 4: Iterate through the items in hm and distribute elements into the buckets based on their freq
        for n,c in hm.items():
            buckets[c].append(n)

        # step 5: Iterate through the buckets from right to left
        # and append elements to the answer list until the desired k 
        # elements are collected
        res = []
        for i in range(len(buckets)-1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
