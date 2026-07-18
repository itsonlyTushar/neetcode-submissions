class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        
        def can_form(index):

            if index == len(s):
                return 1
            
            if index in memo:
                return memo[index]
            
            if s[index] == '0':
                memo[index] = 0
                return 0
            
            ways = can_form(index + 1)


            if index + 1 < len(s):
                two_digita = int(s[index: index + 2])

                if 10 <= two_digita <= 26:
                    ways += can_form(index + 2)
            
            memo[index] = ways
            return ways
        
        return can_form(0)
        
            

            
        