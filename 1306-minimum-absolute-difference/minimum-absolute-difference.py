class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        mindiff = float('inf')

        pairs = []
        arr.sort()
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            if diff < mindiff:
                mindiff = diff
                pairs = []
                pairs.append([arr[i-1], arr[i]])
            elif diff == mindiff:
                pairs.append([arr[i-1], arr[i]])
            print(diff)
        return pairs
                

