class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
            
        left = 0
        right = k-1
        max_len = 0
        while right < len(nums):
            num_ones = nums[right] - nums[left-1] if left > 0 else nums[right]
            curr_len = right - left + 1
            if curr_len - num_ones > k:
                left += 1
            else:
                max_len = max(curr_len, max_len)
                right += 1
                    
        return max_len
        