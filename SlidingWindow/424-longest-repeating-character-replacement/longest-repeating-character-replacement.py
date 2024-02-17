class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        max_value = 0
        output = 0
        left = 0
        for right in range(len(s)):
            right_char = s[right]
            seen[right_char] = seen.get(right_char, 0)+1
            max_val = max(max_value, seen[right_char])

            if (right-left +1 ) - max(seen.values()) > k:
                seen[s[left]] -= 1
                left += 1
            else:
                output = max(output, right-left+1)

        return output