"""

739. Daily Temperatures
Medium
10.5K
237
company
Apple
company
Amazon
company
TikTok
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
Accepted
601.9K
Submissions
908.4K
Acceptance Rate
66.3%

"""

# First attempt


def dailyTemperatures(temperatures: list[int]) -> list[int]:
    res = [0] * len(temperatures)
    for i in range(len(temperatures)):
        for j in range(i + 1, len(temperatures)):

            print(temperatures[i], temperatures[j])
            if temperatures[j] > temperatures[i]:
                res[i] = j - i
                break

    return res

# Optimized


def daily_temps(temperatures: list[int]):
    ans = [0]*len(temperatures)
    stack = []
    for i, temperature in enumerate(temperatures):
        while stack and temperature > temperatures[stack[-1]]:
            index = stack.pop()
            ans[index] = i-index
        stack.append(i)
    return ans


print(dailyTemperatures([30, 60, 90]))
print(dailyTemperatures([30, 40, 50, 60]))
print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
