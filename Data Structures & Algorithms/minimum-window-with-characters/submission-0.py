class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_sub = [-1, -1]
        min_len = float('inf')
        d_s, d_t = {}, {}
        
        for c in t:
            d_s[c] = 0
            d_t[c] = 1 + d_t.get(c, 0)
        
        have, need = 0, len(d_t)
        
        l = 0
        for r in range(len(s)):
            c = s[r]
            if c in d_s:
                d_s[c] += 1
                if d_s[c] == d_t[c]:
                    have += 1

            while have == need:
                if r - l + 1 < min_len:
                    min_sub = [l, r]
                    min_len = r - l + 1

                if s[l] in d_s:
                    d_s[s[l]] -= 1
                    if d_s[s[l]] < d_t[s[l]]:
                        have -= 1

                l += 1

        l, r = min_sub
        return s[l:r + 1] if l != -1 else ""