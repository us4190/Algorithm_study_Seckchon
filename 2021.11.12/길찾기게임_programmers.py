import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class Bst:
    def __init__(self):
        self.head = None
        
    def insert(self, new_node):
        def helper(node):
            if new_node.val < node.val:
                if node.left:
                    helper(node.left)
                else:
                    node.left = new_node
            if new_node.val > node.val:
                if node.right:
                    helper(node.right)
                else:
                    node.right = new_node
        if not self.head:
            self.head = new_node
        else:
            helper(self.head)
            
    def preOrder(self):
        result = []
        def helper(node):
            if not node:
                return
            result.append(node.val)
            helper(node.left)
            helper(node.right)
        
        helper(self.head)
        return result
    
    def postOrder(self):
        result = []
        def helper(node):
            if not node:
                return
            helper(node.left)
            helper(node.right)
            result.append(node.val)
        
        helper(self.head)
        return result
    
def solution(nodeinfo):
    node_dict = {}
    for i in range(len(nodeinfo)):
        node_dict[nodeinfo[i][0]] = i+1
        
    nodes = sorted(nodeinfo, key=lambda x : x[1], reverse=True)
    xList = [i[0] for i in nodes]
    bst = Bst()
    for x in xList:
        bst.insert(Node(x))
    preorder = [node_dict[x] for x in bst.preOrder()]
    postorder = [node_dict[x] for x in bst.postOrder()]
    
    return [preorder, postorder]