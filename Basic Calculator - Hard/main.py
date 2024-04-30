class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # to store numbers and signs
        stack = []
        num = 0
        sign = 1
        result = 0
        
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '+':
                # Apply the previous sign to the current number and add it to the result
                result += sign * num
                # Update sign for the next number
                sign = 1
                # Reset num for the next number
                num = 0
            elif char == '-':
                result += sign * num
                sign = -1
                num = 0
            elif char == '(':
                # Push the current result and sign onto the stack
                stack.append(result)
                stack.append(sign)
                # Reset result and sign for the expression inside parentheses
                result = 0
                sign = 1
            elif char == ')':
                result += sign * num
                # Pop the sign before the open parenthesis
                result *= stack.pop()
                # Add the result before the open parenthesis
                result += stack.pop()
                num = 0
                
        # Add the last number to the result
        result += sign * num
        
        return result
test_cases = [
        "1 + 1",
        " 2-1 + 2 ",
        "(1+(4+5+2)-3)+(6+8)"
    ]
    
solution = Solution()
for idx, test_case in enumerate(test_cases):
    result = solution.calculate(test_case)
    print("Test Case {}: Input: '{}', Output: {}".format(idx+1, test_case, result))
