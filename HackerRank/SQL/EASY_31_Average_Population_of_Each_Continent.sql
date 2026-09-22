-- Given the CITY and COUNTRY tables, query the names of all continents (COUNTRY.Continent) and their respective average city populations (City.Population) rounded down to the nearest integer

SELECT COUNTRY.CONTINENT, FLOOR(AVG(CITY.POPULATION)) FROM COUNTRY JOIN CITY ON COUNTRY.CODE = CITY.COUNTRYCODE GROUP BY COUNTRY.CONTINENT;
