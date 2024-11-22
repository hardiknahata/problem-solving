class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:  # If intervals is empty, just return newInterval
            return [newInterval]

        inserted = False
        for i in range(len(intervals)):
            # Insert newInterval at the correct position
            if intervals[i][0] > newInterval[0]:
                intervals.insert(i, newInterval)
                inserted = True
                break
        
        if not inserted:  # Append newInterval if it wasn't inserted
            intervals.append(newInterval)
        
        merged = []
        for i in range(len(intervals)):
            if not merged:  # Add the first interval
                merged.append(intervals[i])
            elif intervals[i][0] <= merged[-1][1]:  # Merge overlapping intervals
                merged[-1] = [merged[-1][0], max(merged[-1][1], intervals[i][1])]
            else:  # Add non-overlapping intervals
                merged.append(intervals[i])
        
        return merged

# TC = O(n), where n is the number of intervals
# - Insertion of the new interval takes O(n) in the worst case.
# - Merging the intervals also takes O(n), as each interval is processed once.
# SC = O(n), for the resulting merged intervals list.