UPDATE Salary
SET sex 
= CASE sex
WHEN 'f' THEN 'm'
WHEN 'm' THEN 'f'
ELSE sex
END
WHERE sex IN('f', 'm');