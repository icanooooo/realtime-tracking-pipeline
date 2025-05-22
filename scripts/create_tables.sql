-- USERS table
CREATE TABLE IF NOT EXISTS users ( 
	id SERIAL PRIMARY KEY,
	username TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- STATION table
CREATE TABLE IF NOT EXISTS station ( 
	id SERIAL PRIMARY KEY,
	name TEXT NOT NULL,
	city TEXT NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- DESTINATIONS table
CREATE TABLE IF NOT EXISTS destinations ( 
	id SERIAL PRIMARY KEY,
	station_id INT REFERENCES station(id),	
	name TEXT NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ORDERS table
CREATE TABLE IF NOT EXISTS orders ( 
	id SERIAL PRIMARY KEY,
	user_id INT REFERENCES users(id),
	order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	destination_id INT REFERENCES destinations(id)
);

-- ORDERS_HISTORY table
CREATE TABLE IF NOT EXISTS orders_history ( 
	id SERIAL PRIMARY KEY,
	orders_id INT REFERENCES orders(id),
	status TEXT NOT NULL CHECK (status in ('pending', 'packed', 'shipped', 'delivered')),
	location TEXT,
	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


