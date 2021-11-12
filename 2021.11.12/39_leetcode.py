class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()
        
        def backtracking(idx, r, comb):
            c = candidates[idx]
            if r == c:
                answer.append(comb + [c])
            if r > c:
                backtracking(idx, r-c, comb + [c])
                if idx < len(candidates)-1:
                    backtracking(idx+1, r, comb)
                
        backtracking(0, target, [])
        return answer