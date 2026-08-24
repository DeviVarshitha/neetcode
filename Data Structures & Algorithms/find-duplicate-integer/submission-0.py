        
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Step 1: Initialize tortoise and hare to find the intersection point
        tortoise = nums[0]
        hare = nums[0]
        
        # Move tortoise by 1 step and hare by 2 steps until they meet
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
                
        # Step 2: Find the entrance to the cycle (the duplicate number)
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
            
        return tortoise
