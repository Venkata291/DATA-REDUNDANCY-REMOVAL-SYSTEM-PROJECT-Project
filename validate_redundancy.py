from database import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("""
SELECT *
FROM employees
ORDER BY id
""")

rows = cur.fetchall()

print("\n==============================================")
print(" CLOUD DATABASE - UNIQUE VERIFIED RECORDS ")
print("==============================================\n")

for row in rows:

    print(
        f"{row[0]} | "
        f"{row[1]} | "
        f"{row[2]}"
    )

print("\n==============================================")
print("TOTAL UNIQUE RECORDS :", len(rows))
print("==============================================")

cur.close()
conn.close()
