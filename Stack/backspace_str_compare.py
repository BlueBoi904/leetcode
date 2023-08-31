def backspace_compare(s: str, t: str) -> bool:
    def build(stringy):
        stack = []
        for c in stringy:
            if c != "#":
                stack.append(c)
            elif stack:
                stack.pop()
        return "".join(stack)

    return build(s) == build(t)


print(backspace_compare("ab#c", "ad#c"))  # => True
