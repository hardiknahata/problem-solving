import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []  # Initialize a min-heap
        for num in nums:
            heapq.heappush(minheap, num)  # Add the current number to the heap
            if len(minheap) > k:  # Maintain the heap size to k
                heapq.heappop(minheap)  # Remove the smallest element
        
        return minheap[0]  # The root of the heap is the kth largest element

# TC = O(n log k), where n is the size of nums, and k is the size of the heap
# SC = O(k), for storing the k largest elements in the heap