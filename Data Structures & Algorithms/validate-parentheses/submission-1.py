class Solution:
    def isValid(self, s:str) -> bool:
        stack = []

        for ch in s:
            if ch in "({[":
                stack.append(ch)

            else:
                if not stack:  # stack is empty
                    return False

                top = stack.pop()

                if (ch == ')' and top != '(') or \
                   (ch == '}' and top != '{') or \
                   (ch == ']' and top != '['):
                   return False

        # stack should be empty at the end
        return len(stack) == 0
