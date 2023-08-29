def next_great_ele(nums1: list[int], nums2: list[int]) -> list[int]:
    stack = []
    next_greater = {}
    result = []

    # Find the next greater element for each element in nums2
    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)

    # Handle elements in nums1 using the next_greater dictionary
    for num in nums1:
        result.append(next_greater.get(num, -1))

    return result


print(next_great_ele([4, 1, 2], [1, 3, 4, 2]))  # => [-1,3,-1]
