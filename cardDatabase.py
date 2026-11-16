import sqlite3

def databaseInsert(url, name, price, avgDailySold, setName):

    conn = sqlite3.connect("cardDatabase.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cards (
            url TEXT PRIMARY KEY,
            name TEXT,
            price FLOAT,
            avgSold INTEGER,
            setName TEXT
        )
    """)
    cursor.execute(
                """
                INSERT INTO cards (url, name, price, avgSold, setName) 
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(url) DO UPDATE SET
                name = excluded.name,
                setName = excluded.setName
                """,
                (url, name, price, avgDailySold, setName)
            )
    conn.commit()
    conn.close()

def databaseGet():
    conn = sqlite3.connect("cardDatabase.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cards")

    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    conn.close()
