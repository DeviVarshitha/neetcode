
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Count the frequency of each element
        count = Counter(nums)
        
        # Create buckets where index represents the frequency
        # The maximum possible frequency is the length of nums
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count.items():
            buckets[freq].append(num)
            
        # Collect the top k frequent elements from right to left
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Count the frequency of each element
        count = Counter(nums)
        
        # Create buckets where index represents the frequency
        # The maximum possible frequency is the length of nums
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count.items():
            buckets[freq].append(num)
            
        # Collect the top k frequent elements from right to left
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
