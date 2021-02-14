# Exercise 1 ---------------------


CREATE TABLE items(
 id SERIAL PRIMARY KEY,
 item VARCHAR (50) NOT NULL,
 price SMALLINT NOT NULL
)

CREATE TABLE customer(
 id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL
 last_name VARCHAR (50) NOT NULL
)

# Ex2 ----------

INSERT into items (item, price)
values 
('Small Desk', 100), 
('Large Desk', 300), 
('Fan', 80)


INSERT into customers (first_name, last_name)
values 
('Greg', 'Jones'), 
('Sandra', 'Jones'), 
('Scott', 'Scott')
('Trevor', 'Green')
('Melanie', 'Johnson')

# ex 3 --------------

SELECT * FROM public.items
ORDER BY id ASC

SELECT * FROM public.items
where price > 80

SELECT * FROM public.items
where price < 300

SELECT * FROM public.customers
where last_name = 'Smith'
# (no answer)

SELECT * FROM public.customers
where last_name = 'Jones'

SELECT * FROM public.customers
where first_name != 'Scott'

# ------------------------------
<!-- XP Gold - Ex1 -->

INSERT INTO students (first_name, last_name, birth_date)
VALUES 
('Marc', 'Benichou', '1998-11-02'),
('Yoan', 'Cohen', '2010-12-03'),
('Lea','Benichou', '1987-07-27'),
('Amelia', 'Dux', '1996-04-07'),
('David', 'Grez', '2003-06-14'),
('Omer', 'Simpson', '1980-10-03')

SELECT * FROM public.students
ORDER BY id ASC 

SELECT last_name, first_name FROM students

SELECT * FROM public.students
WHERE ID = 2 

SELECT last_name, first_name FROM students
WHERE last_name = 'Benichou' AND first_name = 'Marc' 

SELECT last_name, first_name FROM students
WHERE last_name = 'Benichou' OR first_name = 'Marc'

AND must match exact search, 
OR searches or last_name or first_name giving  multiple results. 

SELECT first_name FROM students
WHERE first_name LIKE '%a%' 

SELECT first_name FROM students
WHERE first_name LIKE 'A%' 

SELECT first_name FROM students
WHERE first_name LIKE '%a' 

SELECT first_name FROM students
WHERE first_name LIKE '%a_'

SELECT * FROM students
WHERE ID = 1 OR ID = 3 

SELECT first_name, last_name, birth_date FROM students
WHERE birth_date >= '1-01-2000'