class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = lambda x: x[1])[::-1]
        
        total_units = 0
        for boxes, units in boxTypes:
            box_count = min(truckSize, boxes)
            total_units += box_count * units
            truckSize -= box_count
            
            if truckSize == 0:
                break
        return total_units

