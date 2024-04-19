# Input: s = "()"
# Output: true

# Input: s = "()[]{}"
# Output: true

# Input: s = "(]"
# Output: false
 
def valid_parentheses(s):
    stack = []
    pair = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
    for i in s:
        if i in pair:
            stack.append(i)
        elif len(stack) == 0 or i != pair[stack.pop()]:
            return 0
    return len(stack) == 0


s = "()[]{}"
print(valid_parentheses(s))