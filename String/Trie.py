# Trie

class node(object):
    def __init__(self, key, data = None):
        self.key = key
        self.data = data
        self.child = {}

class trie(object):
    def __init__(self):
        self.head = node(None)
    def insert(self, s):
        cur = self.head
        for i in s:
            if (i not in cur.child):
                cur.child[i] = node(i)
            cur = cur.child[i]
        cur.data = s
    def search(self, s):
        cur = self.head
        for i in s:
            if (i in cur.child):
                cur = cur.child[i]
            else:
                return False
        if (cur.data != None):
            return True

def main():
    Trie = trie()
    
    for i in ['he', 'she', 'him', 'her', 'shop']:
        Trie.insert(i)

    print(Trie.search('him'))
    print(Trie.search('not'))

if __name__ == "__main__":
    main()
    
