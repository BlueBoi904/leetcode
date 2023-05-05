
# First attempt

class Solution:
    def __init__(self) -> None:
        pass

    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        chars = list(s)

        def left_shift():
            temp = chars.pop(0)
            chars.append(temp)

        def right_shift():
            temp = chars.pop()
            chars.insert(0, temp)

        for arr in shift:
            direction = arr[0]
            amount = arr[1]

            if direction == 0:
                for i in range(amount):
                    left_shift()

            else:
                # Direction will be 1
                for i in range(amount):
                    right_shift()

        return "".join(chars)

# Optimized solution


def string_shift():
    res = 0
    for d, a in shift:
        if d & 1:
            res += a
        else:
            res -= a

    res %= len(s)

    return s[-res:] + s[:-res]
