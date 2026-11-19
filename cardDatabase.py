import sqlite3

def databaseInsert(url, name, price, avgDailySold, setName):

    MAX_CARDS = 50
    PRICE_THRESHOLD = 10

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
        #existing card
        newBase = row[0] if row[0] else price  # keep the existing baseline
        pctChange = (price - newBase) / newBase * 100 if newBase else 0
        if abs(pctChange) >= PRICE_THRESHOLD:
            print("Price Change")
            newBase = price
        else:
            print("Price Goes down")
            newBase = price
    else:
        #non-existing card
        cursor.execute("SELECT COUNT(*) FROM cards")
        if cursor.fetchone()[0] >= MAX_CARDS:
            cursor.execute("SELECT url FROM cards ORDER BY avgSold")
            row = cursor.fetchone()
            cursor.execute("DELETE FROM cards WHERE url = ?", row[0])

    cursor.execute(
                """
                INSERT INTO cards (url, name, price, basePrice, avgSold, setName) 
                VALUES (?, ?, ?, ?, ?, ?)
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
