-- Query the sum of Northen Latitudes (LAT_N) from STATION having values greater than 38.7880 and less than 137.2345. Truncate the answer to 4 decimal places.

SELECT TRUNCATE(SUM(STATION.LAT_N), 4) FROM STATION WHERE STATION.LAT_N > 38.7880 and STATION.LAT_N < 137.2345;
