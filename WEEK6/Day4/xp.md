## Basic Select Statement

### 1. Write a query to display the names (first_name, last_name) using an alias name “First Name”, “Last Name” from employee table.

SELECT first_name AS "First Name", last_name AS "Last Name" FROM employees

### 2. Write a query to get a unique department ID from employee table.
SELECT DISTINCT department_id FROM employees

### 3.Write a query to get the details of all employees from the employee table in descending order by their first name.

SELECT * FROM employees
ORDER BY first_name DESC

### 4. Write a query to get the names (first_name, last_name), salary and 15% of salary as PF (ie. alias) for all the employees.

SELECT first_name, last_name, salary, salary*0.15 AS "PF" FROM employees

### 5. Write a query to get the employee ID, names (first_name, last_name) and salary in ascending order according to their salary.

SELECT employee_id, first_name || ' ' || last_name AS names, salary FROM employees
ORDER BY salary ASC

### 6. Write a query to get the total salaries paid to the employees.

SELECT SUM(salary) FROM employees

### 7. Write a query to get the maximum and minimum salary paid to the employees.

SELECT MAX(salary), MIN(salary) FROM employees

### 8. Write a query to get the average salary paid to the employees.
SELECT AVG(salary) FROM employees 

### 9. Write a query to get the number of employees working in the company.

SELECT COUNT(first_name) FROM employees

### 10. Write a query to get all the first name from the employees table in upper case.
SELECT UPPER(first_name) FROM employees

### 11.  Write a query to get the first three characters of the first name for all the employees in the employees table.

SELECT SUBSTRING("first_name", 1,3) FROM employees

### 12.  Write a query to get the full name of all the employees from employees table. You have to include the first name and last name

SELECT 
CONCAT("first_name", ' ', "last_name") 
AS "Full Name" 
FROM employees

### 13.  Write a query to get the first name, last name and the length of the full name of all the employees from employees table.

SELECT length(CONCAT(first_name, last_name)), first_name, last_name FROM employees


### 14. Write a query to check whether the first_name column of the employees table containing any number.

select * from employees 
where first_name ~ '(?:\d+[a-z]|[a-z]+\d)[a-z\d]*';

select * from employees where first_name ~ '\d';

### 15. Write a query to select first ten records from a table.

SELECT * FROM employees
LIMIT 10


------------------------------------------
## Restricting And Sorting

### 1. Write a query to display the name, including first_name and last_name and salary for all employees whose salary is between $10,000 and $15,000.

SELECT 
CONCAT("first_name", ' ', "last_name") 
AS Name, salary FROM employees
WHERE salary BETWEEN 10000 AND 15000

### 2. Write a query to display the name, including first_name and last_name and hire date for all employees who were hired in 1987.

SELECT 
CONCAT("first_name", ' ', "last_name") AS Name, hire_date
FROM employees
WHERE hire_date BETWEEN '1987-01-01' AND '1987-12-31'

### 3. Write a query to get the first name of the employees who holds the letter ‘c’ and ‘e’ in the first name.

SELECT first_name FROM employees 
WHERE first_name LIKE '%c%' AND first_name LIKE '%e%'

### 4.  Write a query to display the last name, job, and salary for all the employees who don’t work as a Programmer or a Shipping Clerk, and not drawing the salary $4,500, $10,000, or $15,000. 

SELECT last_name, job_title, salary FROM employees
JOIN jobs 
ON jobs.job_id = employees.job_id
WHERE job_title NOT IN ('Programmer', 'Shipping Clerk') 
AND salary NOT IN (4500, 10000, 15000)

### 5. Write a query to display the last names of employees whose last name contain exactly six characters.

SELECT last_name FROM employees
WHERE length(last_name) = 6

### 6. Write a query to display the last name of employees having ‘e’ as the third character.

# STUCK 
SELECT last_name FROM employees
WHERE SUBSTRING(last_name, 3) LIKE '___e'

### 7. Write a query to display the jobs/designations available in the employees table.

SELECT * FROM employees
JOIN jobs
ON employees.job_id = jobs.job_id

### 8. Write a query to select all information of employees whose last name is either ‘JONES’ or ‘BLAKE’ or ‘SCOTT’ or ‘KING’ or ‘FORD’.

SELECT * FROM employees
WHERE last_name 
IN ('Blake','Jones', 'Scott', 'King', 'Ford')