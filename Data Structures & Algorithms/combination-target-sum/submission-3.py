class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        combinations = []

        def bactrack(start_index, remaining_target):
            if remaining_target == 0:
                result.append(combinations.copy())
                return
            
            if remaining_target < 0:
                return
            
            for i in range(start_index, len(nums)):
                combinations.append(nums[i])
                bactrack(i, remaining_target - nums[i])
                combinations.pop()
        bactrack(0, target)
        return result