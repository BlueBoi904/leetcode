/*

Table: Tweets

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
tweet_id is the primary key for this table.
This table contains all the tweets in a social media app.

 

Write an SQL query to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.

Return the result table in any order.

The query result format is in the following example.

 

*/

Create table Tweets
(
    tweet_id int,
    content varchar(50)
)
Truncate table Tweets
insert into Tweets
    (tweet_id, content)
values
    ('1', 'Hello')
insert into Tweets
    (tweet_id, content)
values
    ('2', 'Let us make America great again!')

SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15