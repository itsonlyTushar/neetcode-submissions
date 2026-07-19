class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []

        combinations = []

        def backtrack(index, remain):
            if remain == 0:
                result.append(combinations.copy())
                return
            
            if remain < 0:
                return

            for i in range(index, len(candidates)):

                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                combinations.append(candidates[i])
                backtrack(i + 1, remain - candidates[i])
                combinations.pop()
 
        backtrack(0, target)
        return result