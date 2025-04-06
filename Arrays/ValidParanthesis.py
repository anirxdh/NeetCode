#easy

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack

if __name__ == "__main__":
    s = Solution()
    # Example usage:      
    print(s.isValid("()")) # True
    print(s.isValid("()[]{}")) # True
    print(s.isValid("(]")) # False
