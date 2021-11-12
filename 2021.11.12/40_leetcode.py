class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        answer = []
        
        def backtracking(idx, r, comb, notContain):
            c = candidates[idx]
            if r == c:
                answer.append(comb + [c])
            if r > c and idx < len(candidates)-1:
                if c not in notContain:
                    backtracking(idx+1, r-c, comb + [c], notContain)
                backtracking(idx+1, r, comb, notContain + [c])
        
        backtracking(0, target, [], [])
        return answer
                