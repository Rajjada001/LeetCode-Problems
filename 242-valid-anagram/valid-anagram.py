class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # base condition
        if len(s)!=len(t):
            return False
        countA = [0]*26
        countB = [0]*26
        for char in s:
            countA[ord(char) - ord('a')] += 1
        for char in t:
            countB[ord(char)- ord('a')] += 1

        for i in range(25):
            if countA[i] != countB[i]:
                return False
        return True