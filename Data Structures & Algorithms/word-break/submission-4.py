class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        memo = {}

        def can_break(start_index):
            if start_index == len(s):
                return True
            

            if start_index in memo:
                return memo[start_index]

            for end_index in range(start_index + 1, len(s) + 1):
                current = s[start_index:end_index]

                if current in word_set and can_break(end_index):
                    memo[start_index] = True
                
                    return True
            
            memo[start_index] = False
            return False

        return can_break(0)