def remove_duplicates(s: str):
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)


print(remove_duplicates("abbaca"))  # => "ca"
