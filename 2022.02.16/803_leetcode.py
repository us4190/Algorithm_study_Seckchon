class UnionFind: 
    
    def __init__(self, n): 
        self.parent = list(range(n))
        self.rank = [1] * n
        
    def find(self, p): 
        if p != self.parent[p]: 
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
    
    def union(self, p, q):
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt: return False 
        if self.rank[prt] > self.rank[qrt]: prt, qrt = qrt, prt
        self.parent[prt] = qrt
        self.rank[qrt] += self.rank[prt]
        return True 


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0]) # dimensions 
        
        seen = set()
        for i, j in hits: 
            if grid[i][j]: 
                seen.add((i, j))
                grid[i][j] = 0
        
        uf = UnionFind(m*n+1)
        for i in range(m): 
            for j in range(n): 
                if i == 0 and grid[i][j]: uf.union(j, m*n)
                if grid[i][j]: 
                    for ii, jj in (i-1, j), (i, j-1): 
                        if 0 <= ii < m and 0 <= jj < n and grid[ii][jj]: uf.union(i*n+j, ii*n+jj)
        
        ans = []
        prev = uf.rank[uf.find(m*n)]
        for i, j in reversed(hits): 
            if (i, j) in seen: 
                grid[i][j] = 1
                if i == 0: uf.union(j, m*n)
                for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                    if 0 <= ii < m and 0 <= jj < n and grid[ii][jj]: uf.union(i*n+j, ii*n+jj)
                rank = uf.rank[uf.find(m*n)]
                ans.append(max(0, rank - prev - 1))
                prev = rank
            else: ans.append(0)
        return ans[::-1]