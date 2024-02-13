class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(ch for ch in s if ch.isalnum())
        s1 = s1.lower()
        return s1==s1[::-1]