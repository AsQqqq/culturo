IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname='culturo') THEN
  -- пользователь уже существует, пропускаем создание
ELSE
    CREATE USER culturo WITH PASSWORD 'PP5YGQQ1llKrHRKVFs';
END IF;


IF EXISTS (SELECT 1 FROM pg_catalog.pg_database WHERE datname='culturo') THEN
  -- база данных уже существует, пропускаем создание
ELSE
    CREATE DATABASE culturo;
END IF;

CREATE TABLE accounts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    registration_date VARCHAR(255) NOT NULL
);