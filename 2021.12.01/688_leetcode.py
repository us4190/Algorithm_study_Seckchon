class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if k == 0:
            return 1
        
        dxdy = [
            [1,2],
            [2,1],
            [2,-1],
            [1,-2],
            [-1,-2],
            [-2,-1],
            [-2,1],
            [-1,2]
        ]
        
        cache = [[[0] * k for _ in range(n)] for _ in range(n)]
        
        for l in range(k):
            for i in range(n):
                for j in range(n):
                    prob = 0
                    for dx, dy in dxdy:
                        new_i = i + dx
                        new_j = j + dy
                        if self.isValid(n, new_i, new_j):
                            addProb = cache[new_i][new_j][l-1] if l > 0 else 1
                            prob += addProb
                    prob /= 8
                    cache[i][j][l] = prob
                    
        return cache[row][column][k-1]
                        
    def isValid(self, n, i, j):
        if i < 0 or j < 0:
            return False
        if i >= n or j >= n:
            return False
        return True