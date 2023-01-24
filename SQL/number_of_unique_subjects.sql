SELECT teacher_id, count(DISTINCT subject_id) as cnt
FROM Teacher
GROUP BY teacher_id