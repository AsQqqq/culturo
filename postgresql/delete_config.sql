-- Удаление базы данных, если она существует
DO $$ 
DECLARE
  db_exists BOOLEAN;
BEGIN
  SELECT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'culturo') INTO db_exists;

  IF db_exists THEN
    -- Завершаем все подключения к базе данных
    EXECUTE 'SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE pg_stat_activity.datname = ''culturo''';
  END IF;
END $$;

-- Выполняем DROP DATABASE
DROP DATABASE IF EXISTS culturo;

-- Удаление роли, если она существует
DO $$ 
DECLARE
  role_exists BOOLEAN;
BEGIN
  SELECT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'culturopro') INTO role_exists;
  
  IF role_exists THEN
    -- Сначала отменяем зависимости от роли
    EXECUTE 'REASSIGN OWNED BY culturopro TO postgres';
    
    -- Затем удаляем роль
    DROP ROLE IF EXISTS culturopro;
  END IF;
END $$;