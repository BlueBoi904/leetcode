class Solution:
    def average(self, salary: list[int]) -> float:
        salary.pop(salary.index(min(salary)))
        salary.pop(salary.index(max(salary)))

        return sum(salary) / len(salary)
