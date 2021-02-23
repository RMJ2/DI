### 1. Write a SQL statement to change the email and commission_pct column of the employees table with ‘not available’ and 0.10 for all employees for those employees whose department_id is 110

No column named commission_pct


### 2. Write a SQL statement to change the email column of the employees table with ‘available’ for those employees who belongs to the ‘Accounting’ department.

select first_name, email, department_name from employees
JOIN jobs
ON jobs.job_id = employees.job_id
JOIN departments
ON departments.department_id = employees.department_id
WHERE department_name in ('Accounting')



UPDATE departments SET email =  Available
WHERE department_name IN ('Accounting')