# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:

# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

# Time complexity: O(n)
# Space Complexity: O(n)





class Solution:
    def isValid(self, s: str) -> bool:
        symbol_hash={
             ')':'(',
             '}':'{',
            ']': '['
        }
        stack=[]
        for i in s:
            if i in symbol_hash:
                if stack and stack[-1]== symbol_hash[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False

        




        