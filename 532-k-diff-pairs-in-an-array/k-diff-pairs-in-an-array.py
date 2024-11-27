from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        counts = Counter(nums)  # Count the frequency of each number in the list

        for num in counts:
            if k > 0 and num + k in counts:  # If k > 0, check if the pair (num, num+k) exists
                ans += 1
            elif k == 0 and counts[num] > 1:  # If k == 0, check if there are duplicates of num
                ans += 1

        return ans  # Return the total number of unique pairs

# TC = O(n), where n is the number of elements in nums (constructing Counter is O(n), and iteration is O(n))
# SC = O(n), for the Counter dictionary storing the frequency of elements