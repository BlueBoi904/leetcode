"""



"""

# First attempt, success but sloppy solution


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good_int = []
        size = len(num)
        max_num = -1000
        # looping till length - 2
        for i in range(size - 2):

            # checking the conditions
            if num[i] == num[i + 1] and num[i + 1] == num[i + 2]:

                # printing the element as the
                # conditions are satisfied
                good_int.append(num[i: i + 3])
        if good_int == []:
            return ""
        for num in good_int:
            max_num = max(max_num, int(num))
        res = str(max_num)
        if res == '0':
            return '000'
        return res


def largest_good_int(num: str):
    nums = []
    for i in range(0, len(num)-2):
        if num[i] == num[i+1] == num[i+2]:
            nums.append(num[i:i+3:1])

    if len(nums) == 0:
        return ""
    nums.sort()
    return nums[-1]
