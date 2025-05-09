CREATE DATABASE IF NOT EXISTS gestion_licencias;

USE gestion_licencias;

CREATE TABLE roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

INSERT INTO roles (id, nombre) VALUES
(1, 'Administrador'),
(2, 'Usuario');

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    rol_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (rol_id) REFERENCES roles(id)
);


CREATE TABLE licencias_medicas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_licencia VARCHAR(50) NOT NULL UNIQUE,
    rut_paciente VARCHAR(12) NOT NULL,
    nombre_paciente VARCHAR(100) NOT NULL,
    diagnostico TEXT NOT NULL,
    fecha_emision DATE NOT NULL,
    fecha_inicio_reposo DATE NOT NULL,
    fecha_fin_reposo DATE NOT NULL,
    medico_tratante VARCHAR(100) NOT NULL,
    institucion_emisora VARCHAR(100) NOT NULL,
    estado VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

