"""

1491. Average Salary Excluding the Minimum and Maximum Salary
Easy
988
118
company
Amazon
Netsuite
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.



Example 1:

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500
Example 2:

Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000


Constraints:

3 <= salary.length <= 100
1000 <= salary[i] <= 106
All the integers of salary are unique.
Accepted
160.3K
Submissions
254.8K
Acceptance Rate
62.9%
Seen this question in a real interview before?
1/4
Yes
No
Related Topics

"""


class Solution:
    def average(self, salary: List[int]) -> float:
        total = 0
        n_len = len(salary) - 2
        for i, num in enumerate(sorted(salary)):
            if i != 0 and i != len(salary) - 1:
                total += num
        average = total / n_len
        return average
