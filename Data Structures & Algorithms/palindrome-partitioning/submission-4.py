class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        current_partition = []

        def is_palindrom(sub):
            return sub == sub[::-1]

        def backtrack(start):
            if start == len(s):
                result.append(current_partition.copy())
                return
            
            for end in range(start + 1, len(s) + 1):
                peice = s[start:end]
                if is_palindrom(peice):
                    current_partition.append(peice)
                    backtrack(end)
                    current_partition.pop()
        backtrack(0)
        return result