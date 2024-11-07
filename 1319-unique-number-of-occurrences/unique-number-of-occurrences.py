class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ctr = {}
        unique = set()

        for num in arr:
            if num not in ctr:
                ctr[num] = 1
            else:
                ctr[num] += 1

        for key, freq in ctr.items():
            if freq not in unique:
                unique.add(freq)
            else:
                return False

        return True