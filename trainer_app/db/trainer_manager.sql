DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS trainers;



CREATE TABLE trainers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR (255),
    last_name VARCHAR (255)
);

CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR (255),
    last_name VARCHAR (255),
    age INT,
    trainer_id INT REFERENCES trainers(id)
);