class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        wstart = 0
        wsum = 0.0
        maxAvg = float(-inf)

        for wend in range(len(nums)):
            wsum += nums[wend]

            if wend >= k - 1:
                avg = wsum / k
                if avg > maxAvg:
                    maxAvg = avg
                wsum -= nums[wstart]
                wstart+=1
        return maxAvg


