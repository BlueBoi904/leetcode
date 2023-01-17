"""

You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.

"""


def sort_people(names: list[str], heights: list[int]):
    return [x for _, x in sorted(zip(heights, names), reverse=True)]


# => ["Mary","Emma","John"]
print(sort_people(["Mary", "John", "Emma"], [180, 165, 170]))
# => ["Bob","Alice","Bob"]
print(sort_people(["Alice", "Bob", "Bob"], [155, 185, 150]))
