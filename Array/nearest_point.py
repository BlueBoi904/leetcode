"""

1779. Find Nearest Point That Has the Same X or Y Coordinate
Easy
613
121
company
DoorDash
company
Amazon
You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y). You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi). A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.

Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location. If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.

The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).



Example 1:

Input: x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
Output: 2
Explanation: Of all the points, only [3,1], [2,4] and [4,4] are valid. Of the valid points, [2,4] and [4,4] have the smallest Manhattan distance from your current location, with a distance of 1. [2,4] has the smallest index, so return 2.
Example 2:

Input: x = 3, y = 4, points = [[3,4]]
Output: 0
Explanation: The answer is allowed to be on the same location as your current location.
Example 3:

Input: x = 3, y = 4, points = [[2,3]]
Output: -1
Explanation: There are no valid points.


Constraints:

1 <= points.length <= 104
points[i].length == 2
1 <= x, y, ai, bi <= 104

"""


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        smallest_manhattan = float('inf')
        valid_points = {}
        for i, arr in enumerate(points):
            temp_distance = abs(x - arr[0]) + abs(y - arr[1])
            smallest_manhattan = min(temp_distance, smallest_manhattan)
            if arr[0] == x or arr[1] == y:
                valid_points[i] = smallest_manhattan
        sorted_d = sorted(valid_points.items(), key=operator.itemgetter(1))
        if not valid_points:
            return -1
        else:
            return sorted_d[0][0]
