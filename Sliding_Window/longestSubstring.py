# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def longestSubstring(s):
    left=res = 0
    charSet = set()
    for right in range(len(s)):
        
        while s[right] in charSet:
            charSet.remove(s[left])
            left+=1
        charSet.add(s[right])

        res = max(res,right-left+1) # r-l+1 => size of the substring
    
    return res


print(longestSubstring('abcabcababababaihfh'))
print(longestSubstring('codewiithraj'))
print(longestSubstring('masaajaasa'))
print(longestSubstring('abcabcdbb'))