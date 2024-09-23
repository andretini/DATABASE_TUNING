CREATE DATABASE TUNNING;
USE TUNNING;
-- Tabela de usuários
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefone_usuario VARCHAR(11),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de roles
CREATE TABLE roles (
    role_id INT AUTO_INCREMENT PRIMARY KEY,
    role_name VARCHAR(50) NOT NULL UNIQUE
);

-- Tabela intermediária que associa usuários a múltiplas roles
CREATE TABLE user_roles (
    user_id INT,
    role_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (role_id) REFERENCES roles(role_id),
    PRIMARY KEY (user_id, role_id)
);
