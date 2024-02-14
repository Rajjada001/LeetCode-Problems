class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        q = deque()
        for ch in s:
            if ch in q:
                while q.popleft() != ch:
                    pass
            q.append(ch)
            count = max(len(q), count)
        return count