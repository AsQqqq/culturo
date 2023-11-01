-- Создание роли пользователя 'culturo'
CREATE ROLE culturo WITH LOGIN PASSWORD 'PP5YGQQ1llKrHRKVFs';

-- Создание базы данных 'culturo'
CREATE DATABASE culturo;

GRANT CONNECT ON DATABASE culturo TO culturo;
GRANT ALL PRIVILEGES ON DATABASE culturo TO culturo;
ALTER ROLE culturo LOGIN;

-- Изменение текущей базы данных на 'culturo'
\connect culturo;

-- Создание таблицы 'accounts'
CREATE TABLE IF NOT EXISTS accounts (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    registration_date TIMESTAMP NOT NULL
);