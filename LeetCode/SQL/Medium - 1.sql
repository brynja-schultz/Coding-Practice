# Write your MySQL query statement below
SELECT Employee.name
FROM Employee
JOIN (
    SELECT managerId
    FROM Employee
    GROUP BY managerID
    HAVING COUNT(*) >= 5
) AS m
    ON Employee.id = m.managerId;
