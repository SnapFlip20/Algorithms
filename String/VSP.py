# solution of valid parenthesis string problem

def isBalanced(s):
    opened = ['(', '{', '[']
    closed = [')', '}', ']']
    pair = {'(':')', '{':'}', '[':']'}
    stack = []
    for i in range(len(s)):
        if s[i] in opened:
            stack.append(s[i])
        elif s[i] in closed:
            if len(stack) == 0:
                return False
            elif (len(stack) > 0 and pair[stack.pop()] != s[i]):
                return False
    return not bool(stack)
