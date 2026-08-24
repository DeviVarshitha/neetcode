class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # If mid element is greater than the rightmost element,
            # the minimum element must be in the right half.
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise, the minimum element is at mid or to its left.
            else:
                right = mid
                
        return nums[left]
