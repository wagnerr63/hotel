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
	date DATE NOT NULL,
	hour FLOAT,
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