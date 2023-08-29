def make_great(s: str):
    stack = []

    for c in s:
        if stack and stack[-1].lower() == c.lower() and c != stack[-1]:
            stack.pop()
        else:
            stack.append(c)

    return ''.join(stack)
