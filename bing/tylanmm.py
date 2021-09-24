from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

class TrieNode:
    def __init__(self):
        self.next = [None]*26
        self.amt = 0
    
    def add(self, word):
        self.amt += 1
        if word:
            c = ord(word[0]) - 97
            if not self.next[c]:
                self.next[c] = TrieNode()
            return self.next[c].add(word[1:])
        return self.amt

n = int(_i())
root = TrieNode()
for i in range(n):
    word = _i()
    _p(root.add(word) - 1)

stdout.flush()