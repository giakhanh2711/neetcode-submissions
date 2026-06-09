class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_len = 0
        count = {chr(asci): 0 for asci in range(ord('A'), ord('A') + 27)}
        
        for r in range(len(s)):
            count[s[r]] += 1
            
            while r - l + 1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len