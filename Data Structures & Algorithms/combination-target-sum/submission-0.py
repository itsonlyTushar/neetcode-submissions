class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        current_combination = []

        def backtrack(start_index, remaining_target):
            if remaining_target == 0:
                result.append(current_combination.copy())
                return
            
            if remaining_target < 0:
                return
            
            for i in range(start_index, len(nums)):
                current_combination.append(nums[i])
                
                backtrack(i, remaining_target - nums[i])

                current_combination.pop()

        backtrack(0, target)
        return result 