import MySQLdb as mysql
import random
import mariadb

def get_db(user, password):
    """connecting database (change user and password for testing)"""
    yhteys = mysql.connect(
        host = 'localhost',
        port = 3306,
        database = 'flight_game',
        user = "python",
        password = "huihai",
        autocommit = True
    )
    return yhteys

def get_starting_airport(connection, first_country):
    """randomizing starting airport from users choice"""
    sql = """
        SELECT airport.name, country.name, airport.latitude_deg, airport.longitude_deg
        FROM airport 
        JOIN country ON country.iso_country = airport.iso_country
        WHERE country.name = %s
        AND airport.type = 'medium_airport' 
        AND scheduled_service = 'yes'
    """
    cursor = connection.cursor()
    cursor.execute(sql, (first_country,))
    result = cursor.fetchall()
    return random.choice(result)

def get_two_airports(connection, next_country):
    """
    returns two random airports from given country.
    returns list: (ident, name, country, lat, lon)
    """
    sql = """
        SELECT airport.name, country.name, 
               airport.latitude_deg, airport.longitude_deg
        FROM airport
        JOIN country ON country.iso_country = airport.iso_country
        WHERE country.name = %s
          AND airport.type IN ('medium_airport','large_airport')
          AND scheduled_service = 'yes'
    """
    cursor = connection.cursor()
    cursor.execute(sql, (next_country,))
    result = cursor.fetchall()
    if len(result) < 2:
        return None
    return random.sample(result, 2)

def get_items(connection):
    sql = """
          SELECT items.id, \
                 items.name,
                 items.danger_level, \
                 items.description, \
                 items.security_class
          FROM items
    """
    cursor = connection.cursor()
    cursor.execute(sql)
    items = [
        {
            "id": row[0],
            "name": row[1],
            "danger_level": row[2],
            "description": row[3],
            "security_class": row[4]
        }
        for row in cursor.fetchall()
    ]
    return items
