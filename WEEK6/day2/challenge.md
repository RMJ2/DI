CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
)

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar')

SELECT * FROM FirstTab

CREATE TABLE SecondTab (
    id integer 
)

INSERT INTO SecondTab VALUES
(5),
(NULL)


SELECT * FROM SecondTab

## Q1. What will be the OUTPUT of the following statement?
### Count = 0
SELECT COUNT(*) 
FROM FirstTab a WHERE a.Id NOT IN ( SELECT Id FROM SecondTab WHERE Id IS NULL )

## Q2. What will be the OUTPUT of the following statement?
### count = 2
SELECT COUNT(*) 
FROM FirstTab a WHERE a.Id NOT IN ( SELECT Id FROM SecondTab WHERE Id = 5 )

## Q3. What will be the OUTPUT of the following statement?
### count = 0
SELECT COUNT(*) 
FROM FirstTab a WHERE a.Id NOT IN ( SELECT Id FROM SecondTab )

## Q4. What will be the OUTPUT of the following statement?
### count = 2
SELECT COUNT(*) 
FROM FirstTab a WHERE a.Id NOT IN ( SELECT Id FROM SecondTab WHERE Id IS NOT NULL )