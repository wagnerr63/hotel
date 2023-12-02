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
VALUES
  ('Maria Santos', '(11) 98765-4321', 'maria@example.com', '1985-10-20', '98765432102'),
  ('Pedro Oliveira', '(22) 5555-5555', 'pedro@example.com', '1995-03-08', '55555555503'),
  ('Ana Souza', '(33) 1112-2233', 'ana@example.com', '1980-12-25', '11122233304'),
  ('Carlos Lima', '(44) 7777-8888', 'carlos@example.com', '1977-09-14', '77788899905'),
  ('Mariana Vieira', '(55) 33333-3333', 'mariana@example.com', '1992-07-30', '33333333306'),
  ('Rafael Ferreira', '(66) 4444-4444', 'rafael@example.com', '1988-02-12', '44444444407');

INSERT INTO room (name, description, qty_beds, qty_restrooms, hydromassage, price)
VALUES ('Quarto Standard', 'Quarto confortável com TV e ar condicionado', 2, 1, false, 100.00);

INSERT INTO room (name, description, qty_beds, qty_restrooms, hydromassage, price)
VALUES ('Suíte de Luxo', 'Suíte espaçosa com vista para o mar e banheira de hidromassagem', 1, 1, true, 250.00);
INSERT INTO room (name, description, qty_beds, qty_restrooms, hydromassage, price)
VALUES
  ('Suíte Master', 'Suíte luxuosa com vista panorâmica', 1, 1, true, 250.00),
  ('Quarto Deluxe', 'Quarto espaçoso com varanda', 2, 1, false, 150.00),
  ('Quarto Econômico', 'Quarto simples e confortável', 1, 1, false, 80.00),
  ('Suíte Familiar', 'Suíte ideal para famílias', 3, 2, true, 300.00),
  ('Quarto Executivo', 'Quarto com área de trabalho', 1, 1, false, 120.00),
  ('Suíte Presidencial', 'A suíte mais luxuosa do hotel', 2, 2, true, 500.00);

INSERT INTO activity (name, description, local)
VALUES ('Passeio de Barco', 'Passeio relaxante pela costa', 'Pier A');

INSERT INTO activity (name, description, local)
VALUES ('Caminhada na Praia', 'Caminhada matinal pela praia', 'Praia Principal');
INSERT INTO activity (name, description, local)
VALUES
  ('Trilha na Floresta', 'Trilha emocionante na natureza', 'Parque Nacional'),
  ('Aula de Mergulho', 'Aprenda a mergulhar com instrutores experientes', 'Centro de Mergulho B'),
  ('Passeio de Bicicleta', 'Explore a cidade de bicicleta', 'Bicicletaria XYZ'),
  ('Degustação de Vinhos', 'Prove vinhos locais em nossa adega', 'Adega do Hotel'),
  ('Aula de Surfe', 'Aprenda a surfar com instrutores certificados', 'Praia C'),
  ('Passeio de Helicóptero', 'Desfrute de vistas panorâmicas da cidade', 'Heliporto Z');

INSERT INTO reservation (description, id_client, date, employee)
VALUES ('Reserva de férias', 1, '2023-07-15 14:00:00', 'Ana Silva');

INSERT INTO reservation (description, id_client, date, employee)
VALUES ('Viagem de Aniversário', 2, '2023-08-10 12:00:00', 'Carlos Souza');
INSERT INTO reservation (description, id_client, date, employee)
VALUES
  ('Aniversário de Casamento', 2, '2023-08-20 16:30:00', 'Carlos Santos'),
  ('Fim de Semana Relaxante', 3, '2023-09-10 12:00:00', 'Mariana Oliveira'),
  ('Viagem de Negócios', 4, '2023-07-30 10:15:00', 'Rafael Ferreira'),
  ('Lua de Mel', 5, '2023-10-05 18:00:00', 'Isabela Lima'),
  ('Férias em Família', 6, '2023-08-12 15:45:00', 'Pedro Vieira'),
  ('Retiro Espiritual', 7, '2023-09-25 09:30:00', 'João Almeida');

INSERT INTO reservation_room (id_room, id_reservation)
VALUES (1, 1);  -- Quarto Standard para a primeira reserva

INSERT INTO reservation_room (id_room, id_reservation)
VALUES (2, 2);  -- Suíte de Luxo para a segunda reserva

INSERT INTO client_activity (id_client, id_activity, date)
VALUES (1, 1, '2023-07-16 10:00:00');  -- Cliente 1 participando de Passeio de Barco

INSERT INTO client_activity (id_client, id_activity, date)
VALUES (2, 2, '2023-08-11 08:30:00');  -- Cliente 2 participando de Caminhada na Praia
