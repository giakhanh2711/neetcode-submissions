class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        l = 0
        hashmap = {}

        for r in range(len(s)):
            while s[r] in hashmap and hashmap[s[r]] != 0:
                hashmap[s[l]] = 0
                l += 1
            
            hashmap[s[r]] = 1
            max_len = max(max_len, r - l + 1)
        
        return max_len