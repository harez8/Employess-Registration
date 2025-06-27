CREATE TABLE employee (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_surname VARCHAR(20) NOT NULL,
    second_surname VARCHAR(20) NOT NULL,
    first_name VARCHAR(20) NOT NULL,
    other_names VARCHAR(50),
    country VARCHAR(20) NOT NULL,
    id_type VARCHAR(30) NOT NULL,
    id_number VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(300) NOT NULL UNIQUE,
    entry_date DATE NOT NULL,
    area VARCHAR(50) NOT NULL,
    status VARCHAR(20) DEFAULT 'ACTIVO',
    created_at DATETIME NOT NULL
);
