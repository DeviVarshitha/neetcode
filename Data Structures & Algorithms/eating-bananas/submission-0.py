import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            # Calculate total hours needed with an eating rate of 'mid'
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / mid)
                
            # If Koko can finish within h hours, try a smaller rate
            if total_hours <= h:
                ans = mid
                high = mid - 1
            else:
                # If it takes too long, increase the eating rate
                low = mid + 1
                
        return ans
