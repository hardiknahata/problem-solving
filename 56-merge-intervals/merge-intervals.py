class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        if len(intervals) == 1:
            return intervals
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= merged[-1][1]:
                merged[-1] = [merged[-1][0], max(intervals[i][1], merged[-1][1])]
            else:
                merged.append(intervals[i])

        return merged