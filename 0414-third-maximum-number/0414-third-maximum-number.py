class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)
        nums_sort = sorted(s,reverse = True)
        if len(nums_sort) < 3:
            return max(nums_sort)
        else:
            return nums_sort[2]
        
        
        