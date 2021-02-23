CREATE TABLE orders(
id SERIAL PRIMARY KEY,
customer VARCHAR,
contact BIGINT,
price INT
car_id INT
)

CREATE TABLE items(
id SERIAL PRIMARY KEY,
car_brand VARCHAR,
model VARCHAR,
price INT
)

INSERT INTO items (id, car_brand, model, price)
VALUES
(1,'vw', 'golf', 20000),
(2,'ford', 'fiesta', 18000),
(3,'vauxhall', 'corsa', 15000),
(4,'porsche', '911', 70000),
(5,'tesla', 'model 3', 50000),
(6,'hummer', 'h1', 90000),
(7,'ferrari', 'dino', 500000)


INSERT INTO orders (id, customer, contact, price, car_id)
VALUES
(1, 'Joshua Phillips', 058555555, 70000, 4),
(2,'Harry Harris', 058544444, 18000, 2),
(3,'Sam Levine', 0585533333, 15000, 3),
(4,'Adam Schwartz', 0585111111, 500000, 7),
(5,'Jordan Phillips', 05877777, 70000, 4)