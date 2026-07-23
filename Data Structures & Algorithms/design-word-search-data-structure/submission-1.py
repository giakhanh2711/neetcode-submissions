class Word:
    def __init__(self):
        self.children = {}
        self.is_end_word = False

class WordDictionary:

    def __init__(self):
        self.root = Word()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = Word()
            cur = cur.children[w]
        cur.is_end_word = True

    def search(self, word: str) -> bool:
        def dfs(cur, i_word):
            for i in range(i_word, len(word)):
                w = word[i]
                if w == '.':
                    for k in cur.children:
                        if dfs(cur.children[k], i + 1):
                            return True
                    return False
                if w not in cur.children:
                    return False
                
                cur = cur.children[w]
            
            return cur.is_end_word
        
        return dfs(self.root, 0)
