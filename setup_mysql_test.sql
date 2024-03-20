-- A script that prepares a MYSQL server for the project
-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create user hbnb_test
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grnt select on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- flush to apply changes
FLUSH PRIVILEGES;
