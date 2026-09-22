-- Query the greatest value of the Northen Latitudes (LAT_N) from STATION that is less than 137.2345. Truncate the answer to 4 decimal places.

SELECT TRUNCATE(MAX(STATION.LAT_N), 4) FROM STATION WHERE STATION.LAT_N < 137.2345;
