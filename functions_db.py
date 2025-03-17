import sqlite3
conn  = sqlite3.connect("avtosalon.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cars  (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand   TEXT NOT NULL,
        model   TEXT NOT NULL,
        info    TEXT NOT NULL,
        logo    TEXT NOT NULL,
        image   TEXT NOT NULL
    );
""")


def create_new_car(brand, model, info, logo, image):
    cursor.execute(""" 
        INSERT INTO cars (brand, model, info, logo, image) 
        VALUES (?,?,?,?,?)""", 
        (brand, model, info, logo, image))
    conn.commit()

def all_cars():
    cursor.execute("""
        SELECT * FROM cars;
    """)
    cars  = cursor.fetchall()
    return cars

car_id = 1

def delete_car(car_id):
    cursor.execute(""" DELETE FROM cars WHERE id = ?""", (car_id,))
    conn.commit()

# print(cars)
brand, model, info, logo, image = "BYD", "SONG PLUS", "the chine car ", "cherry_logo", "cherry_image"

# create_new_car(brand, model, info, logo, image)

cars = all_cars()
print(cars)

conn.commit()
conn.close()


