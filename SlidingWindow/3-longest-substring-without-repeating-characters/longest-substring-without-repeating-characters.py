class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        output = 0
        for right in range(len(s)):
            c = s[right]
            if c in seen and seen[c] >= left:
                left = seen[c] + 1
            else:
                output = max(output, right-left+1)
            seen[c] = right
        
            # print(seen, left, right)
        return output
