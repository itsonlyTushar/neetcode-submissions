class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        combinations = []

        def backtrack(index, remain):
            if remain == 0:
                result.append(combinations.copy())
                return
            
            if remain < 0:
                return
            
            for i in range(index, len(nums)):
                combinations.append(nums[i])
                backtrack(i, remain - nums[i])
                combinations.pop()
        backtrack(0, target)
        return result