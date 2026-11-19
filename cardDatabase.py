import sqlite3

def databaseInsert(url, name, price, avgDailySold, setName):

    priceThreshold = 0
    conn = sqlite3.connect("cardDatabase.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cards (
            url TEXT PRIMARY KEY,
            name TEXT,
            price FLOAT,
            basePrice FLOAT,
            avgSold INTEGER,
            setName TEXT
        )
    """)
    cursor.execute("SELECT basePrice FROM cards WHERE url = ?", (url,))
    row = cursor.fetchone()

    newBase = price

    if row is not None:
        newBase = row[0] if row[0] else price  # keep the existing baseline
        pctChange = (price - newBase) / newBase * 100

    cursor.execute(
                """
                INSERT INTO cards (url, name, price, avgSold, setName) 
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(url) DO UPDATE SET
                name = excluded.name,
                price = excluded.price,
                basePrice = excluded.basePrice,
                avgSold = excluded.avgSold,
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
