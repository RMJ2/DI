Use joins (inner, left right, outer)
on the address, city and country tables.
to display the street address, city name and country name. 

### INNER JOIN
address.address
city.city
country.country 

SELECT address.address, city.city, country.country
FROM country

INNER JOIN city
ON city.country_id = country.country_id

INNER JOIN address
ON address.city_id = city.city_id

### RIGHT JOIN
SELECT city.city, country.country
FROM country

RIGHT JOIN city
ON city.country_id = country.country_id


### LEFT JOIN
SELECT city.city, country.country
FROM country

LEFT JOIN city
ON city.country_id = country.country_id