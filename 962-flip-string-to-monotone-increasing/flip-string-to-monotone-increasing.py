class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        total_zeros = sum(1 for c in s if c=="0")
        flips = total_zeros

        min_flips = flips
        for ch in s:
            if ch == "0":
                flips -= 1
            else:
                flips += 1
            
            min_flips = min(flips, min_flips)
    
        return min_flips
