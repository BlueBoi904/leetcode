"""

2225. Find Players With Zero or One Losses
Medium
1.1K
81
company
Indeed
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.


Example 1:

Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
Example 2:

Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].


Constraints:

1 <= matches.length <= 105
matches[i].length == 2
1 <= winneri, loseri <= 105
winneri != loseri
All matches[i] are unique.
Accepted
69.9K
Submissions
94.5K
Acceptance Rate
74.0%
Seen this question in a real interview before?
1/4
Yes
No  

"""

# First attempt successfull, 98% Time Complexity.


def find_winners(matches: list[list[int]]):
    loss_counts = {}
    ans = [[], []]

    for match in matches:
        match_winner = match[0]
        match_loser = match[1]

        if match_winner not in loss_counts:
            loss_counts[match_winner] = 0

        if match_loser in loss_counts:
            loss_counts[match_loser] += 1
        else:
            loss_counts[match_loser] = 1
    for key in loss_counts:
        if loss_counts[key] == 0:
            ans[0].append(key)

        if loss_counts[key] == 1:
            ans[1].append(key)
    ans[0].sort()
    ans[1].sort()
    return ans


find_winners([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [
             4, 5], [4, 8], [4, 9], [10, 4], [10, 9]])  # => [[1,2,10],[4,5,7,8]]

find_winners([[2, 3], [1, 3], [5, 4], [6, 4]])  # => [[1,2,5,6],[]]
