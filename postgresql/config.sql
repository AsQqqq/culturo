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

-- Создание таблицы 'places'
CREATE TABLE places (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    photo_path VARCHAR(255) NOT NULL, -- Это поле будет хранить путь к папке с фотографиями
    description TEXT NOT NULL,
    hours_of_operation TEXT NOT NULL,
    contact_phone VARCHAR(20) NOT NULL,
    location POINT -- POINT может использоваться для хранения координат местонахождения, но это опционально
);


GRANT INSERT,UPDATE,DELETE ON TABLE public.accounts TO culturo; -- Allow culturo to write to table_2
GRANT SELECT ON TABLE public.places TO culturo; -- Allow culturo to read table_1

-- Создание роли пользователя 'culturopro'
CREATE ROLE culturopro WITH LOGIN PASSWORD 'EptGvfiHh1KVkpKS-Qkn';

-- Добавление прав доступа к базе данных 'culturo'
GRANT CONNECT ON DATABASE culturo TO culturopro;
GRANT USAGE ON SCHEMA public TO culturopro;

-- Добавление прав доступа к таблице 'places'
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE public.places TO culturopro;

-- Запрет доступа к другим таблицам
REVOKE ALL PRIVILEGES ON TABLE public.accounts FROM culturopro;

-- Изменение текущей базы данных на 'culturo'
\connect culturo;

-- Подключение роли 'culturopro' к текущей сессии
SET ROLE culturopro;