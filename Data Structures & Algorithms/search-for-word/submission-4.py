class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nums_rows = len(board)
        nums_cols = len(board[0])


        def search(row, col, word_index):
            if word_index == len(word):
                return True
            
            if row < 0 or row >= nums_rows or col < 0 or col >= nums_cols:
                return False
            
            if board[row][col] != word[word_index]:
                return False
            
            og_letter = board[row][col]
            board[row][col] = "*"

            found = (
                search(row + 1, col, word_index + 1)
                or
                search(row - 1, col, word_index + 1)
                or
                search(row, col + 1, word_index + 1)
                or
                search(row, col - 1, word_index + 1)
            )

            board[row][col] = og_letter
            return found
        
        for row in range(nums_rows):
            for col in range(nums_cols):
                if search(row, col, 0):
                    return True
        return False