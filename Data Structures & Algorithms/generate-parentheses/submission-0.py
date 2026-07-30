class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(cnt_open, cnt_close, cur_str, cur_open):
            if len(cur_str) == n + n:
                res.append(cur_str)
                return

            if cnt_open > 0:
                backtrack(cnt_open - 1, cnt_close, cur_str + "(", cur_open + 1)
            if cur_open > 0:
                backtrack(cnt_open, cnt_close - 1, cur_str + ")", cur_open - 1)

        backtrack(n, n, "", 0)

        return res