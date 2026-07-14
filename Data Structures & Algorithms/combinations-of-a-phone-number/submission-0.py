class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        } 
        
        result = []

        def backtrack(index, combinations):
            if index == len(digits):
                result.append("".join(combinations))
                return
            
            possible_letters = phone[digits[index]]

            for letter in possible_letters:
                combinations.append(letter)
                backtrack(index + 1, combinations)
                combinations.pop()

        
        
        backtrack(0, [])
        return result