class Solution:
    def minSwaps(self, data: List[int]) -> int:
        total_ones = sum(data)  # Total number of 1s in the array
        if total_ones == 0 or total_ones == 1:
            return 0  # No swaps needed if no or only one 1 exists
        
        # Initialize the sliding window
        current_ones = sum(data[:total_ones])  # Count 1s in the first window of size total_ones
        max_ones_in_window = current_ones  # Track the max 1s in any window
        
        # Slide the window across the array
        for i in range(total_ones, len(data)):
            current_ones += data[i] - data[i - total_ones]  # Update the window count
            max_ones_in_window = max(max_ones_in_window, current_ones)  # Update the max
        
        # Minimum swaps needed to group all 1s together
        return total_ones - max_ones_in_window

# TC: O(n), single pass to calculate total_ones and another pass for the sliding window
# SC: O(1), constant space used for variables