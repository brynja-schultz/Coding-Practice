-- Query the Western Longitude (LONG_W) for the largest North Latitude (LAT_N) in STATION that is less than 137.2345. Round the answer to 4 decimal places.

SELECT ROUND(STATION.LONG_W, 4) FROM STATION WHERE STATION.LAT_N = (SELECT MAX(STATION.LAT_N) FROM STATION WHERE LAT_N < 137.2345);
