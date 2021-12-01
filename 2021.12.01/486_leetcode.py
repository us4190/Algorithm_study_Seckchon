class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0:
            return True
        
        l = len(nums)
        cache = [[0] * l for _ in range(l)]
        
        def dp(cache, i, j):
            if cache[i][j] != 0:
                return cache[i][j]
            
            if i == j:
                cache[i][j] = [nums[i], 0]
                return [nums[i], 0]
            
            length = j - i + 1
            
            fst_s1, fst_s2 = dp(cache, i+1, j)
            snd_s1, snd_s2 = dp(cache, i, j-1)
            if length % 2 == 1:
                fst = fst_s1 + nums[i] - fst_s2
                snd = snd_s1 + nums[j] - snd_s2
                if fst > snd:
                    cache[i][j] = [fst_s1 + nums[i], fst_s2]
                else:
                    cache[i][j] = [snd_s1 + nums[j], snd_s2]
                    
            else:
                fst = fst_s2 + nums[i] - fst_s1
                snd = snd_s2 + nums[j] - snd_s1
                if fst > snd:
                    cache[i][j] = [fst_s1, fst_s2 + nums[i]]
                else:
                    cache[i][j] = [snd_s1, snd_s2 + nums[j]]
            return cache[i][j]
                    
        p1, p2 = dp(cache, 0, l-1)
        return p1-p2 >= 0