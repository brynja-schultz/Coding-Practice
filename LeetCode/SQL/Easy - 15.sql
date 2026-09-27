# Write your MySQL query statement below
SELECT id AS Id
FROM (
    SELECT
        id,
        recordDate,
        temperature,
        LAG(recordDate) OVER (ORDER BY recordDate) AS previous_date,
        LAG(temperature) OVER (ORDER BY recordDate) AS previous_value
    FROM Weather
) t
WHERE temperature > previous_value
    AND DATEDIFF(recordDate, previous_date) = 1;
