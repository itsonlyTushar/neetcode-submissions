class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        two_back = 0

        for cash in nums:
            rob = two_back + cash
            new_best = max(rob, prev)

            two_back = prev
            prev = new_best

        return prev