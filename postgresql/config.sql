-- Создание роли 'culturopro', если она не существует
DO $$ 
BEGIN
  IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'culturopro') THEN
    CREATE ROLE culturopro WITH LOGIN PASSWORD 'EptGvfiHh1KVkpKS-Qkn';
  END IF;
END $$;

-- Подключение к базе данных 'postgres' или другой существующей базе перед созданием новой базы данных
\connect postgres;

-- Создание базы данных 'culturo', если она не существует
CREATE DATABASE culturo;

-- Подключение к базе данных 'culturo'
\connect culturo;

-- Проверка существования таблицы 'accounts' и создание, если не существует
CREATE TABLE IF NOT EXISTS accounts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    registration_date TIMESTAMP NOT NULL,
    save BOOLEAN DEFAULT FALSE,
    tested BOOLEAN DEFAULT FALSE,
    common_location VARCHAR(255), 
    user_id VARCHAR(255) NOT NULL,
    token VARCHAR(255)
);

-- Проверка существования таблицы 'places' и создание, если не существует
CREATE TABLE IF NOT EXISTS places (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    name_photo VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    hours_of_operation_start TEXT,
    hours_of_operation_end TEXT,
    contact_phone VARCHAR(20),
    email VARCHAR(255),
    date_open VARCHAR(255),
    common_location VARCHAR(255),
    location VARCHAR(255),
    site VARCHAR(255),
    break_time_start VARCHAR(255),
    break_time_end VARCHAR(255),
    estimation INTEGER DEFAULT(100),
    id_point VARCHAR(255) NOT NULL
);

-- Проверка существования таблицы 'code' и создание, если не существует
CREATE TABLE IF NOT EXISTS code (
    id SERIAL PRIMARY KEY,
    code VARCHAR(255) NOT NULL,
    login VARCHAR(255) NOT NULL,
    activate BOOLEAN DEFAULT TRUE
);

-- Предоставление прав доступа к таблице 'accounts' для роли 'culturopro'
GRANT ALL PRIVILEGES ON TABLE accounts TO culturopro;

-- Предоставление прав доступа к таблице 'places' для роли 'culturopro'
GRANT ALL PRIVILEGES ON TABLE places TO culturopro;

-- Предоставление прав доступа к таблице 'code' для роли 'culturopro'
GRANT ALL PRIVILEGES ON TABLE code TO culturopro;

-- Предоставление прав доступа к всем последовательностям в схеме public для роли 'culturopro'
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO culturopro;

-- Подключение к базе данных 'postgres' или другой существующей базе перед созданием новой базы данных
\connect postgres;

-- Создание базы данных 'culturoplace', если она не существует
CREATE DATABASE culturoplace;