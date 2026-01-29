import mysql.connector

DB_CONFIG = {
	"host": "127.0.0.1",
	"port": 3306,
	"user": "admin",
	"password": "admin",
	"database": "flight_game"
}

def get_airport_amounts(connection, iso_country):
	cursor = connection.cursor()
	query = f"SELECT type, COUNT(*) AS airport_count FROM {DB_CONFIG["database"]}.airport WHERE iso_country=\"{iso_country}\" GROUP BY iso_country, type ORDER BY airport_count DESC, type"

	cursor.execute(query)

	rows = cursor.fetchall()
	cursor.close()
	return rows

def print_rows(rows):
	if rows == []:
		print("Not found")
		return

	for i in rows:
		print(f"{i[0]}: {i[1]}")

def main():
	connection = mysql.connector.connect(**DB_CONFIG)

	iso_country = input("Enter country code (e.g FI, US): ")
	rows = get_airport_amounts(connection, iso_country)
	print_rows(rows)

main()