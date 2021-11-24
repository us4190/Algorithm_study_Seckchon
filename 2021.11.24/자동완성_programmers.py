class Node:
    def __init__(self, count):
        self.count = count
        self.charDict = {}

class Trie:
    def __init__(self):
        self.head = Node(0)
        
    def insert(self, word):
        node = self.head
        for c in word:
            if c in node.charDict:
                node = node.charDict[c]
                node.count += 1
            else:
                node.charDict[c] = Node(1)
                node = node.charDict[c]
        node.charDict['*'] = None

    def dfs(self):
        node = self.head
        stack = [node]
        count = 0
        while stack:
            node = stack.pop()
            count += node.count
            if node.count != 1:
                for key in node.charDict:
                    if key != '*':
                        stack.append(node.charDict[key])
        return count

def solution(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    answer = trie.dfs()
    return answer