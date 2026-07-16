class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n <= 2:
            return 1
        
        first, second, third = 0, 1,1
        for _ in range(3, n + 1):
            next_value = first + second + third
            first, second, third = second, third, next_value
        return third
        