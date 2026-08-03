class Solution:

    def check_palindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False   
            start += 1
            end -= 1
        return True


    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(cur_partitions, start_par):
            if start_par >= len(s):
                # tmp = [x for x in cur_partitions]
                res.append(cur_partitions.copy())
                return
            
            for i in range(start_par, len(s)):
                if self.check_palindrome(s, start_par, i):
                    cur_partitions.append(s[start_par:i + 1])
                    backtrack(cur_partitions, i + 1)
                    cur_partitions.pop()
        
        backtrack([], 0)
        
        return res
        