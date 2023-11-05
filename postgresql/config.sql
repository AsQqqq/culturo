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
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    registration_date TIMESTAMP NOT NULL
);

-- Создание таблицы 'places'
CREATE TABLE IF NOT EXISTS places (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    photo_path VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    hours_of_operation TEXT NOT NULL,
    contact_phone VARCHAR(20) NOT NULL,
    location POINT
);

-- Создание таблицы 'code'
CREATE TABLE IF NOT EXISTS code (
    id SERIAL PRIMARY KEY,
    code VARCHAR(255) NOT NULL,
    login VARCHAR(255) NOT NULL,
    activate BOOLEAN DEFAULT TRUE
);


REVOKE ALL PRIVILEGES ON TABLE public.accounts FROM cuturo; -- Запрещаем всё в accounts
REVOKE ALL PRIVILEGES ON TABLE public.code FROM cuturo; -- Запрещаем всё в code
GRANT SELECT ON TABLE public.places TO culturo; -- Разрешаем только читать данные из places

-- Создание роли пользователя 'culturopro'
CREATE ROLE culturopro WITH LOGIN PASSWORD 'EptGvfiHh1KVkpKS-Qkn';

-- Добавление прав доступа к базе данных 'culturo'
GRANT CONNECT ON DATABASE culturo TO culturopro;
GRANT USAGE ON SCHEMA public TO culturopro;

-- Добавление прав доступа к таблице 'places'
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE public.accounts TO culturopro;
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE public.code TO culturopro;
GRANT USAGE, SELECT ON SEQUENCE code_id_seq TO culturopro;
-- GRANT USAGE, SELECT ON SEQUENCE public.code TO culturopro;

-- Запрет доступа к другим таблицам
REVOKE ALL PRIVILEGES ON TABLE public.places FROM culturopro;

-- Изменение текущей базы данных на 'culturo'
\connect culturo;

-- Подключение роли 'culturopro' к текущей сессии
SET ROLE culturopro;