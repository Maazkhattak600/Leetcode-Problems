class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for x in range(n):
            if math.log(n) == math.log(pow(3,x)):
                
                return True
            if pow(3,x) > n:
                
                return False
        