"""

1678. Goal Parser Interpretation
Easy
1.1K
74
company
Apple
company
Amazon
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.



Example 1:

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
Example 2:

Input: command = "G()()()()(al)"
Output: "Gooooal"
Example 3:

Input: command = "(al)G(al)()()G"
Output: "alGalooG"


Constraints:

1 <= command.length <= 100
command consists of "G", "()", and/or "(al)" in some order.

"""


def interpret(command: str):
    # We need to traverse the string, and create a new string
    res = []
    result = [command[i: j] for i in range(len(command))
              for j in range(i + 1, len(command) + 1)]
    # Build res while parsing the command string
    i = 0
    for sub in result:
        if sub == 'G':
            res.append('G')

        if sub == '()':
            res.append('o')

        if sub == '(al)':
            res.append('al')

        # Need to find if this block of chars is () or (al)

        # Return the built command string
    return "".join(res)


def interpret_string(command: str):
    myStr = ''
    cmdLen = len(command)
    i = 0
    command = command+"xxx"
    while i < cmdLen:
        if command[i] == "G":
            myStr = myStr+"G"
            i = i+1
        elif command[i] == "(" and command[i+1] == ")":
            myStr = myStr+"o"
            i = i+2
        elif command[i] == "(" and command[i+1] == "a":
            myStr = myStr+"al"
            i = i+4
    return myStr


def interpret_string_one_liner(command: str):
    return command.replace('()', 'o').replace('(al)', 'al')


interpret("G()(al)")  # => "Goal"
interpret("G()()()()(al)")  # => "Gooooal"
interpret("(al)G(al)()()G")  # => "alGalooG"
