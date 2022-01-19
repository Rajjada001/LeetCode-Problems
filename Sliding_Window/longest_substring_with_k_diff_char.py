def longestSubstringWith_k_diff_char(s,k):
    # base condition
    if k==0:
        return 0
    # define pointer
    l = r = maxLen = 0
    d = {}
    while(r<len(s)):
        d[s[r]] = r
        if len(d)>k:
            min_index = min(d.values())
            l = min_index + 1
            del d[s[min_index]]
        maxLen = max(maxLen, r-l+1)
        r += 1
    return maxLen


print(longestSubstringWith_k_diff_char('ebaca', 2))
print(longestSubstringWith_k_diff_char('ebacaabababadf', 3))
print(longestSubstringWith_k_diff_char('aba', 1))