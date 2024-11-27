from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        if k == len(nums):
            return nums

        count = Counter(nums) # Build a hash map: number and its frequency

        # 2. Find the k most frequent elements using a heap
        # O(N log k) time
        most_frequent = heapq.nlargest(k, count.keys(), key=count.get)

        return most_frequent