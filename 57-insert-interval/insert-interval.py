class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        inserted = False
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                intervals.insert(i, newInterval)
                inserted = True
                break
        if not inserted:
            intervals.append(newInterval)
        
        merged = []
        for i in range(len(intervals)):
            if not merged:
                merged.append(intervals[i])
            elif intervals[i][0] <= merged[-1][1]:
                merged[-1] = [merged[-1][0],max([merged[-1][1], intervals[i][1]])]
            else:
                merged.append(intervals[i])
        
        return merged

