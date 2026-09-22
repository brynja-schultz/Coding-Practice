SELECT DISTINCT CITY FROM STATION WHERE LEFT(CITY, 1) NOT in ('A', 'E', 'I', 'O', 'U') or RIGHT(CITY, 1) NOT in ('a', 'e', 'i', 'o', 'u');
