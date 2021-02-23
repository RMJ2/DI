## Exercise 1: Dvd Rental

### 1. Get a list of all film languages
SELECT * FROM public.language
ORDER BY language_id ASC 

### 2. Get a list of all films joined with their languages – select only the film title, description, and language name. Try your query with different joins:
select film.title, film.description, language.name 
from film
LEFT JOIN language 
ON language.language_id = film.language_id

### Get all films, even if they don’t have languages
select film.title, film.description, language.name 
from film
INNER JOIN language 
ON language.language_id = film.language_id


### Get all languages, even if there are no films in those languages. Which languages are these?
select * from language
"English             "
"Italian             "
"Japanese            "
"Mandarin            "
"French              "
"German              "


### 3.  Create a new table called new_film with the following columns : id, name. Add some new films to the table.

CREATE TABLE new_film(
id serial PRIMARY KEY,
name VARCHAR (50) NOT NULL 
)

### 4.Create a new table called customer_review, to contain data about film reviews that customers will make.
### Think about the DELETE constraint: if a film is deleted, it’s review should be automatically deleted

### It should have the following columns:
### 1. review_id – a primary key, non null, auto-increment
### 2. film_id – references the new_film table. The film that is being reviewed.
### 3. language_id – references the language table. What language the review is in.
### 4. title – the title of the review
### 5. score – the rating of the review (1-10)
### 6. review_text – the text of the review. No limit on the length.
### 7. last_update – when the review was last updated.

CREATE TABLE customer_review(
review_id SERIAL PRIMARY KEY,
film_id SMALLINT, FOREIGN KEY(film_id) REFERENCES film(film_id) ON DELETE CASCADE,
language_id SMALLINT, FOREIGN KEY(language_id) REFERENCES language(language_id),
title VARCHAR(50),
score SMALLINT NOT NULL, 
review_text TEXT,
last_update DATE
)

### 5. Add 2 movie reviews. Make sure you link them to valid objects in the other tables.

insert into customer_review 
(film_id, language_id, title, score, review_text, last_update)
VALUES
(1, 1, 'Fantastic', 5, 'It was shit', now()::DATE),
(2, 1, 'Was alright', 2, 'It was ok', now()::DATE)

### 6. Delete a film that has a review from the new_film table, what happens to the customer_review table?

DELETE from new_film 
Where film_id = 1

## Exercise 2 : Dvd Rental

### 1. Use UPDATE to change the language of some films. Make sure that you use valid languages…

UPDATE film
SET language_id = 3
WHERE film_id = 1

### 2. Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
store_id 
address_id 
it links the columns to the other tables. 

### 3. We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?

YES THAT WAS VERY EASY. 

### 4. Find out how many rentals are still outstanding. (ie. have not been returned to the store yet)

SELECT count(rental_date) - count(return_date) FROM rental 
183

### 5. Mark the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)

Select rental_rate, title, inventory.inventory_id, rental_date from rental 
INNER JOIN inventory
ON inventory.inventory_id = rental.inventory_id
INNER JOIN film 
ON film.film_id = inventory.film_id
WHERE return_date IS NULL
ORDER BY rental_rate DESC LIMIT 30

### 6. Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he is talking about?

### 6.1 The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.

SELECT title, description, first_name, last_name FROM film_actor
JOIN film 
ON film.film_id = film_actor.film_id
JOIN actor 
ON actor.actor_id = film_actor.actor_id
WHERE description LIKE '%Sumo%' AND first_name = 'Penelope' AND last_name = 'Monroe'
ANSWER = 'Park Citizen'

### 6.2 The 2nd film : A short documentary (less than 1 hour long), rated “R”.

SELECT title, name, length FROM film
JOIN film_category
ON film_category.film_id = film.film_id
JOIN category
ON category.category_id = film_category.category_id
WHERE name = 'Documentary' AND length<60 AND rating = 'R'

### 6.3 The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
select title,first_name ,rental_rate,last_name,return_date
from film 
join inventory on
film.film_id =inventory.film_id
join rental on
rental.inventory_id = inventory.inventory_id
join customer on
customer.customer_id =rental.customer_id
where rental_rate>4 and first_name ='Matthew' and last_name='Mahan'
and return_date between '2005-07-28' and '2005-08-01'

### 6.4 The 4th film : His friend Matthew Mahan watched this film, too. It had the word ‘boat’ in the title or description, and it looked like it was a very expensive DVD to replace.

SELECT title, first_name, last_name, description, rental_rate, replacement_cost
FROM film
join inventory on
film.film_id =inventory.film_id
join rental on
rental.inventory_id = inventory.inventory_id
join customer on
customer.customer_id =rental.customer_id
WHERE first_name = 'Matthew' AND last_name = 'Mahan' 
AND description LIKE '%Boat%' OR title LIKE '%boat%'
ORDER BY replacement_cost DESC LIMIT 1

ANSWER = Stone Fire. 

