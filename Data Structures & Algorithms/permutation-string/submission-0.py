class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap_s1 = {}
        for c in s1:
            hashmap_s1[c] = 1 + hashmap_s1.get(c, 0)
        
        l = 0
        for r in range(len(s1) - 1, len(s2)):
            hashmap_s1_tmp = hashmap_s1.copy()
            count = 0
            is_the_same = True
            for c in s2[l:r + 1]:
                if c not in hashmap_s1_tmp or hashmap_s1_tmp[c] == 0:
                    is_the_same = False
                    break
                hashmap_s1_tmp[c] -= 1
                count += 1
            
            l += 1

            if not is_the_same:
                continue
            
            if count == len(s1):
                return True
        
        return False