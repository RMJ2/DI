## We will work on the public database that we created yesterday.

### All items, ordered by price (lowest to highest).
SELECT * FROM items
ORDER BY price ASC

### Items with a price above 80 (80 included), ordered by price (highest to lowest).
SELECT * FROM items
WHERE price >= 80 ORDER BY price ASC

### The first 3 customers in alphabetical order (A-Z) – exclude ‘id’ from the results.
SELECT first_name, last_name FROM customers
ORDER BY first_name ASC LIMIT 3

### All last names (no other columns!), in reverse alphabetical order (Z-A)
SELECT last_name FROM customers
ORDER BY last_name DESC 

### 2. 
### Create a table named purchases. It should have 2 columns : customer_id and item_id. These columns are references from the tables customers and items. Edit the data of the purchases table: 
CREATE TABLE purchases (
customer_id SMALLINT, 
FOREIGN KEY(customer_id) REFERENCES customers(id)
item_id SMALLINT,
FOREIGN KEY(item_id) REFERENCES items(id)
)

### Add a row which references a customer by ID, but does not reference an item by ID (leave it blank). Does this work? Why/why not?
It works, id was input to customers_id in purchases. 
INSERT INTO purchases (customer_id)
VALUES
(1)

### Add 5 rows which reference existing customers and items.
INSERT INTO purchases (customer_id, item_id)
VALUES
(1,2),
(2,1),
(3,3),
(4,2),
(5,3)

## 3.
### All purchases. Is this information useful to us?
SELECT * FROM purchases
(not really relevent as its just numbers. )

### All purchases, joining with the customers table.
SELECT * 
FROM customers
INNER JOIN purchases
ON customers.id = purchases.customer_id

### Purchases of the customer with the ID equal to 4.
SELECT * FROM purchases
WHERE customer_id = 4

### Purchases for a large desk AND a small desk
SELECT * FROM purchases
WHERE item_id IN (1,2)


## 4.
### Create a purchase for Scott Scott – he bought a hard drive.
INSERT INTO items (item, price)
VALUES
('Hard drive', 250)

INSERT INTO purchases (customer_id, item_id)
VALUES 
(3, 4)

## 5. Use SQL to show all the customers who have made a purchase. Show the following fields/columns:

### Customer first name
### Customer last name
### Item name

SELECT customers.first_name, customers.last_name, items.item 
FROM purchases

INNER JOIN items
ON items.id = purchases.item_id

INNER JOIN customers
ON customers.id = purchases.customer_id



<!----------Exercise 2 : Dvdrental Database----------- -->
### Write a query to select all the columns from the table “customer” in the database named dvdrental.
SELECT * FROM customer

### Write a query to display the names (first_name, last_name) using an alias named “full_name”.
SELECT first_name || ' '|| last_name AS full_name FROM customer

### You want to know every date where one or several accounts were created. Write a query to select the dates of creation from the “customer” table, it shouldn’t have duplicates.
SELECT create_date FROM customer
GROUP BY create_date

### Write a query to get the details of all customers from the customer table in descending order by their first name.
SELECT * FROM customer
ORDER BY first_name DESC

### Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.
SELECT film_id, title, description, release_year, rental_rate FROM film
ORDER BY rental_rate ASC

### Write a query to get the address, the district and the phone number from the customers living in the district Texas in the “address” table.
SELECT address, district, phone FROM address
WHERE district = 'Texas'

### Write a query to retrieve the details of the movies with the id 15 and 150.
SELECT * FROM film
WHERE film_id in (15,150)

### Pick your favorite movie. Write a query to see if the rental shop owns it. Write a query to get the film ID, the title, the description, the length and the rental rate from the film table for your movie title.
SELECT film_id, title, description, length, rental_rate FROM film
WHERE title LIKE '_odfather'

### Didn’t find it ? Maybe you made a mistake in the name. Write a query to get the film ID, the title, the description, the length and the rental rate from the “film” table for all the movies starting with the two first letters of your movie.
SELECT film_id, title, description, length, rental_rate FROM film
WHERE title LIKE 'Go%'

### You want to have a choice between ten propositions of movies and you want the cheapest ones. Write a query to find the 10th cheapest movies.
SELECT title FROM film
ORDER BY rental_rate ASC LIMIT 10

### You are not satisfied with the results. Write a query to find the 10th next cheapest movies.
Bonus: Try to not use LIMIT.
SELECT title FROM film
ORDER BY rental_rate ASC OFFSET 10 FETCH NEXT 10 ROW only


### 12. Write a query to join the data of the customer table and the payment table. You want to get the amount and the date of every payment made by a customer, ordered by his id (from 1 to…).
SELECT 
customer.customer_id, customer.first_name, customer.last_name, payment.amount, payment.payment_date
FROM payment

INNER JOIN customer
ON customer.customer_id = payment.customer_id
ORDER BY customer.customer_id ASC

### 13. cannot check as there is no inventory marked 0

### 14. Write a query to find which city is in which country.
SELECT country.country, city.city
FROM city
INNER JOIN country
ON city.country_id = country.country_id