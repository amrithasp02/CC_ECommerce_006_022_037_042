import mysql.connector

#Open database
conn = mysql.connector.connect(user="root", password="totallysecurepass", host="172.19.50.2", db="test")

cursor = conn.cursor()

#Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS users 
		(userId INTEGER PRIMARY KEY AUTO_INCREMENT, 
		password TEXT,
		email TEXT,
		firstName TEXT,
		lastName TEXT,
		address1 TEXT,
		address2 TEXT,
		zipcode TEXT,
		city TEXT,
		state TEXT,
		country TEXT, 
		phone TEXT
		)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS categories
		(categoryId INTEGER PRIMARY KEY,
		name TEXT
		)''')


cursor.execute('''CREATE TABLE IF NOT EXISTS products
		(productId INTEGER PRIMARY KEY,
		name TEXT,
		price REAL,
		description TEXT,
		image TEXT,
		stock INTEGER,
		categoryId INTEGER,
		FOREIGN KEY(categoryId) REFERENCES categories(categoryId)
		)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS kart
		(userId INTEGER,
		productId INTEGER,
		FOREIGN KEY(userId) REFERENCES users(userId),
		FOREIGN KEY(productId) REFERENCES products(productId)
		)''')



conn.close()

