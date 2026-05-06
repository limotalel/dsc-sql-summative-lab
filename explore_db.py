import sqlite3
conn = sqlite3.connect("data.sqlite")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("Tables:", tables)
for t in tables:
    tname = t[0]
    cursor.execute("PRAGMA table_info(" + tname + ")")
    cols = cursor.fetchall()
    print("\n" + tname + ":")
    for c in cols:
        print("  " + c[1] + " (" + c[2] + ")")
    # Sample a few rows
    cursor.execute("SELECT * FROM " + tname + " LIMIT 2")
    rows = cursor.fetchall()
    print("  Sample:", rows)
conn.close()
