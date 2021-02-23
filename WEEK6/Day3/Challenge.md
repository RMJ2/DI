Create Table client(
id SERIAL PRIMARY KEY,
first_name VARCHAR, 
last_name VARCHAR,
teudat_zehut INT,
apartment_no SMALLINT,
building_code SMALLINT,
address VARCHAR
city VARCHAR, 
elevator, VARCHAR,
phone BIGINT,
email VARCHAR,
animal VARCHAR,
active, VARCHAR
);

Create Table animal_info(
animal_id SERIAL PRIMARY KEY,
animal_name VARCHAR,
animal_type VARCHAR,
gender VARCHAR,
age SMALLINT,
dob INT,
weight SMALLINT,
color VARCHAR,
sterilized VARCHAR,
chip VARCHAR
);

Create Table payments(
payment_id SERIAL PRIMARY KEY,
customer_id INT,
animal_id INT,
payment_date date,
amount NUMERIC,
payment_method VARCHAR
)


select * from client
JOIN animal_info
ON animal_info.animal_id = client.id
JOIN payments
ON animal_info.animal_id = payments.animal_id


