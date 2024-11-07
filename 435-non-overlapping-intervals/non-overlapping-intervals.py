class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        remove = 0
        prev = intervals[0][1]

        print(intervals)

        for i in range(1, len(intervals)):
            if intervals[i][0] >= prev:
                prev = intervals[i][1]
                continue
            else:
                print(intervals[i])
                remove += 1

        return remove