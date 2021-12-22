class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if (n == 0):
            return False
        start = 0
        end = n-1

        while (start <= end) :
            mid = (start+end) // 2

            if (nums[mid] == target):
                return True

            if not self.isBinarySearchHelpful(nums, start, nums[mid]):
                start += 1
                continue

            pivotArray = self.existsInFirst(nums, start, nums[mid])
            targetArray = self.existsInFirst(nums, start, target)
            
            if (pivotArray ^ targetArray) :
                if (pivotArray) :
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if (nums[mid] < target):
                    start = mid + 1
                else:
                    end = mid - 1
            
        return False;

    def isBinarySearchHelpful(self, nums, start, element):
        return nums[start] != element
    

    def existsInFirst(self, nums, start, element):
        return nums[start] <= element