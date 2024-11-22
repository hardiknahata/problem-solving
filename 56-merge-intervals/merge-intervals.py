class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals based on the start time
        intervals = sorted(intervals, key=lambda x: x[0])
        
        merged = []  # List to store merged intervals
        for interval in intervals:
            # If merged is empty or there's no overlap, add the interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Merge overlapping intervals by updating the end time
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
        
        return merged  # Return the list of merged intervals

# TC = O(n log n), sorting takes O(nlogn), merging takes a single pass which is O(n)
# SC = O(n), for the merged list to store the output intervals.