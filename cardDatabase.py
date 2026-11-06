import sqlite3

def databaseInsert(name, price, avgDailySold, setName, url):

    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cards (
            name TEXT PRIMARY KEY,
            price TEXT,
            avgSold INTEGER,
            setName TEXT,
            url TEXT
        )
    """)

    cursor.execute(
        "INSERT INTO cards (name, price, avgSold, setName, url) VALUES (?, ?, ?, ?, ?)",
        (name, price, avgDailySold, setName, url)
    )

    conn.commit()
    conn.close()

def dataGet():
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cards")

    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    conn.close()
