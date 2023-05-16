# First attempt, sliding window


class Solution:
    def compress(self, chars: List[str]) -> int:
        curr_char = chars[0]
        curr_count = 1
        write_idx = 0

        # iterate through the characters
        for i in range(1, len(chars)):
            if chars[i] == curr_char:
                # increment the count for the current character
                curr_count += 1
            else:
                # write the compressed version of the current group to the list
                chars[write_idx] = curr_char
                write_idx += 1
                if curr_count > 1:
                    for digit in str(curr_count):
                        chars[write_idx] = digit
                        write_idx += 1
                # reset the variables for the new group
                curr_char = chars[i]
                curr_count = 1

        # write the compressed version of the last group to the list
        chars[write_idx] = curr_char
        write_idx += 1
        if curr_count > 1:
            for digit in str(curr_count):
                chars[write_idx] = digit
                write_idx += 1

        return write_idx


# Optimized solution


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0
        while i < len(chars):
            group_length = 1
            while i + group_length < len(chars) and chars[i + group_length] == chars[i]:
                group_length += 1
            chars[res] = chars[i]
            res += 1
            if group_length > 1:
                str_repr = str(group_length)
                chars[res : res + len(str_repr)] = list(str_repr)
                res += len(str_repr)
            i += group_length
        return res
