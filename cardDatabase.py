import sqlite3

def databaseInsert(name, price, avgDailySold, setName, url):

    conn = sqlite3.connect("cardDatabase.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cards (
            name TEXT PRIMARY KEY,
            price FLOAT,
            avgSold INTEGER,
            setName TEXT,
            url TEXT
        )
    """)
    cursor.execute(
        "SELECT name FROM cards WHERE name = ? AND setName = ?",
        (name, setName)
    )
    card = cursor.fetchone()
    if card:
        cursor.execute(
            "SELECT price FROM cards WHERE name = ? AND setName = ?",
            (name, setName)
        )
        oldPrice = cursor.fetchone()
        increasedPrice = price + (price * .5)
        if oldPrice >= increasedPrice:
            
    else:
        cursor.execute(
            "INSERT INTO cards (name, price, avgSold, setName, url) VALUES (?, ?, ?, ?, ?)",
            (name, price, avgDailySold, setName, url)
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
