class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        
class Bst:
    def __init__(self):
        self.head = None
        
    def insert(self, newNode):
        def helper(node):
            if newNode.val < node.val:
                if node.left:
                    helper(node.left)
                else:
                    node.left = newNode
            if newNode.val > node.val:
                if node.right:
                    helper(node.right)
                else:
                    node.right = newNode
        if not self.head:
            self.head = newNode
        else:
            helper(self.head)

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        bst = Bst()
        for i in nums:
            bst.insert(Node(i))
        
        def count(node):
            mod=(10**9)+7
            if not node:
                return [0,0]
            left_val, left_count = count(node.left)
            right_val, right_count = count(node.right)
            child_count = left_count + right_count
            result = self.factorial(child_count) // self.factorial(left_count) // self.factorial(right_count)
            if left_val > 0:
                result *= left_val
            if right_val > 0:
                result *= right_val
            return [result, child_count+1]
        
        mod=(10**9)+7
        return count(bst.head)[0] % mod - 1
            
    def factorial(self, num):
        if num == 0:
            return 1
        result = 1
        for i in range(1, num+1):
            result *= i
        return result