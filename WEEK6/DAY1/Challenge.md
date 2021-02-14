SELECT count(*) FROM actors

4


INSERT INTO actors (first_name, last_name, age)
VALUES 
('Johnny', 'Bravo', 13)

ERROR:  null value in column "number_oscars" of relation "actors" violates not-null constraint
DETAIL:  Failing row contains (5, Johnny, Bravo, 13, null).
SQL state: 23502