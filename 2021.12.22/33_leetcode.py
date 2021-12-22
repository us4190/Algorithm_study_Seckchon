class Solution:
    def search(self, nums: List[int], target: int) -> int:
        maxIdx = self.findMaxIdx(nums)
        if target < nums[0]:
            left = maxIdx + 1
            right = len(nums) - 1
        else:
            left = 0
            right = maxIdx
            
        answer = -1
        while right >= left:
            mid = (left + right) // 2
            if nums[mid] == target:
                answer = mid
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return answer
        
        
        
    def findMaxIdx(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        left = 0
        right = len(nums) - 1
        
        while right >= left:
            mid = (left + right) // 2
            if nums[mid] > nums[left]:
                if nums[mid] > nums[mid+1]:
                    return mid
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid - 1
            elif nums[left] > nums[right]:
                return left
            else:
                return right        
        raise