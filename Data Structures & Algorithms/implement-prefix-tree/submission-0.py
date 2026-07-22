class Node:
    def __init__(self):
        self.children = [None for _ in range(27)]
        
class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if not cur.children[ord(c) - 97]:
                cur.children[ord(c) - 97] = Node()
            cur = cur.children[ord(c) - 97]
        
        cur.children[-1] = Node()

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if not cur.children[ord(c) - 97]:
                return False
            cur = cur.children[ord(c) - 97]

        return True if cur.children[-1] else False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if not cur.children[ord(c) - 97]:
                return False
            cur = cur.children[ord(c) - 97]
        return True
        
        