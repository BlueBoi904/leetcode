def is_valid(s: str):
    # Create a stack
    stack = []

    # Create a mapping of opening brackets to closing brackets

    matches = {"(": ")", "[": "]", "{": "}"}

    # Iterate over the str, if we spot an opening bracket we put it into the stack.

    # If we spot a closing bracket, we can check the most recent unclosed opening bracket by popping it from the stack.

    # If it matches, continue. If not, or there is no opening bracket on the stack at all then the string is invalid.

    # Our stack must be empty for the string to be valid, having popped off all matching opening brackets with a
    # closing bracket.

    for char in s:
        if char in matches:  # If char is an opening bracket
            stack.append(char)
        else:
            if not stack:  # Check if stack is empty
                return False

            prev_open = stack.pop()

            if matches[prev_open] != char:
                return False

    return not stack


print(is_valid("({})"))  # => True

print(is_valid("(){}[]"))  # => True

print(is_valid("(]"))  # => False

print(is_valid("({)}"))  # => False
