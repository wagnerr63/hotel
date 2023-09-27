-- SQLBook: Code
CREATE TABLE IF NOT EXISTS client(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50),
	phone VARCHAR(20),
	email VARCHAR(50),
	birth_date DATE,
	cpf VARCHAR(20) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS room (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	description VARCHAR(255),
	qty_beds SMALLINT DEFAULT 0,
	qty_restrooms SMALLINT DEFAULT 0,
	hydromassage BOOL DEFAULT false,
	price FLOAT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS activity (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	description VARCHAR(255),
	local VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS reservation (
	id SERIAL PRIMARY KEY,
	description VARCHAR(255),
	id_client INT REFERENCES client(id),
	date TIMESTAMP NOT NULL,
	employee VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS reservation_room (
	id SERIAL PRIMARY KEY,
	id_room INT REFERENCES room(id),
	id_reservation INT REFERENCES reservation(id)
);

CREATE TABLE IF NOT EXISTS client_activity (
	id SERIAL PRIMARY KEY,
	id_client INT REFERENCES client(id),
	id_activity INT REFERENCES activity(id),
	date TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW()
);

INSERT INTO client (name, phone, email, birth_date, cpf)
VALUES ('João Silva', '123-456-7890', 'joao@example.com', '1990-05-15', '12345678901');

INSERT INTO client (name, phone, email, birth_date, cpf)
VALUES ('Maria Santos', '987-654-3210', 'maria@example.com', '1985-08-20', '98765432102');

INSERT INTO room (name, description, qty_beds, qty_restrooms, hydromassage, price)
VALUES ('Quarto Standard', 'Quarto confortável com TV e ar condicionado', 2, 1, false, 100.00);

INSERT INTO room (name, description, qty_beds, qty_restrooms, hydromassage, price)
VALUES ('Suíte de Luxo', 'Suíte espaçosa com vista para o mar e banheira de hidromassagem', 1, 1, true, 250.00);

INSERT INTO activity (name, description, local)
VALUES ('Passeio de Barco', 'Passeio relaxante pela costa', 'Pier A');

INSERT INTO activity (name, description, local)
VALUES ('Caminhada na Praia', 'Caminhada matinal pela praia', 'Praia Principal');

INSERT INTO reservation (description, id_client, date, employee)
VALUES ('Reserva de férias', 1, '2023-07-15 14:00:00', 'Ana Silva');

INSERT INTO reservation (description, id_client, date, employee)
VALUES ('Viagem de Aniversário', 2, '2023-08-10 12:00:00', 'Carlos Souza');

INSERT INTO reservation_room (id_room, id_reservation)
VALUES (1, 1);  -- Quarto Standard para a primeira reserva

INSERT INTO reservation_room (id_room, id_reservation)
VALUES (2, 2);  -- Suíte de Luxo para a segunda reserva

INSERT INTO client_activity (id_client, id_activity, date)
VALUES (1, 1, '2023-07-16 10:00:00');  -- Cliente 1 participando de Passeio de Barco

INSERT INTO client_activity (id_client, id_activity, date)
VALUES (2, 2, '2023-08-11 08:30:00');  -- Cliente 2 participando de Caminhada na Praia
