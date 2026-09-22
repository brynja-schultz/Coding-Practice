-- Query the following two values from the STATION table:

-- The sum of all values in LAT_N rounded to a scale of 2 decimal places
-- The sum of all values in LONG_W rounded to a scale of 2 decimal places

SELECT DECIMAL(ROUND(SUM(LAT_N), 2), 10, 2), DECIMAL(ROUND(SUM(LONG_W), 2), 10, 2) FROM STATION;
