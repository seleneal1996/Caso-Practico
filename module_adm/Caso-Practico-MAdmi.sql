CREATE DATABASE IF NOT EXISTS AdministrationDB;

USE AdministrationDB;

-- Collaborators Table
CREATE TABLE IF NOT EXISTS Collaborators (
    id_colaborador INT PRIMARY KEY,
    nombre VARCHAR(255),
    apellido VARCHAR(255),
    dni VARCHAR(15),
    estado ENUM('activo', 'inactivo') DEFAULT 'activo'
);

-- Contract Types Table
CREATE TABLE IF NOT EXISTS ContractTypes (
    id_contract_type INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    eps BOOLEAN,
    insurance BOOLEAN
);

-- Contacts Table
CREATE TABLE IF NOT EXISTS Contacts (
    id_contact INT PRIMARY KEY AUTO_INCREMENT,
    id_collaborator INT,
    contact_type ENUM('phone', 'email'),
    contact_detail VARCHAR(255),
    FOREIGN KEY (id_collaborator) REFERENCES Collaborators(id_colaborador)
);

-- Contracts Table
CREATE TABLE IF NOT EXISTS Contracts (
    id_contract INT PRIMARY KEY AUTO_INCREMENT,
    id_collaborator INT,
    id_contract_type INT,
    duration VARCHAR(50),
    FOREIGN KEY (id_collaborator) REFERENCES Collaborators(id_colaborador),
    FOREIGN KEY (id_contract_type) REFERENCES ContractTypes(id_contract_type)
);

-- Schedules Table
CREATE TABLE IF NOT EXISTS Schedules (
    id_schedule INT PRIMARY KEY AUTO_INCREMENT,
    id_collaborator INT,
    day_of_week ENUM('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'),
    start_time TIME,
    end_time TIME,
    FOREIGN KEY (id_collaborator) REFERENCES Collaborators(id_colaborador)
);

-- Assignment of Contracts and Schedules Table
CREATE TABLE IF NOT EXISTS Assignments (
    id_assignment INT PRIMARY KEY AUTO_INCREMENT,
    id_contract INT,
    id_schedule INT,
    FOREIGN KEY (id_contract) REFERENCES Contracts(id_contract),
    FOREIGN KEY (id_schedule) REFERENCES Schedules(id_schedule)
);

-- Users Table
CREATE TABLE IF NOT EXISTS Users (
    id_user INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50),
    password VARCHAR(255), -- Passwords should be securely stored using hash functions
    role ENUM('administrator', 'user') DEFAULT 'user',
    id_collaborator INT,
    FOREIGN KEY (id_collaborator) REFERENCES Collaborators(id_colaborador)
);
