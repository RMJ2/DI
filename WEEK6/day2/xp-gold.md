## Exercise 1: DVD Rental 

### Find out how many films there are for each rating
select rating, count(rating) From film 
group by rating


### Get a list of all the movies that have a rating of G or PG-13
select title, rating From film 
where rating = 'PG-13' or rating = 'G' 

### Filter this list further: look for only movies that are under 2 hours long, and whose rental price (rental_rate) is under 3.00. Sort the list alphabetically.

NOT SURE

Find a customer in the customer table, and change his/her details to your details, using SQL UPDATE.




## EXERCISE 2 Students Table

## Update
### ‘Lea Benichou’ and ‘Marc Benichou’ are twins, they should have the same birth_date. Update both their birth_date to 02/11/1998.

update students 
set birth_date = '1998-11-02'
where id in (3,1)

### Change the last_name of David from ‘Grez’ to ‘Guez’.
update students 
set last_name = 'Guez'
where id = 5

## Insert/Alter
### Add a column to the table student, called math_grade.

