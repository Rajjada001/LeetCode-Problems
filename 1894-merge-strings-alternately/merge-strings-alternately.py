class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # brute force
        small, large = '',''
        if len(word1)>len(word2):
            small=word2
            l = word1
        else:
            small=word1
            l = word2
        res = []
        for i in range(len(small)):
            res.append(word1[i])
            res.append(word2[i])
        large = l[len(small):]
        for ch in large:
            res.append(ch)
        return ''.join(ch for ch in res)