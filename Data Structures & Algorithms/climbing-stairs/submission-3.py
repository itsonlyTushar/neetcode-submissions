class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        

        two_steps = 1
        one_step = 1

        for step in range(2, n + 1):
            current = two_steps + one_step
            two_steps = one_step
            one_step = current
        return one_step