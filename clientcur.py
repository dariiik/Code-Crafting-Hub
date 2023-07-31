import psycopg2 
import time as t
con = psycopg2.connect(
    host = "darigasmac", 
    database = "darigaid", 
    user = "postgres", 
    password = "postgres")

#client side cursor
s = t.time()
cur = con.cursor()
e = (t.time() - s)*1000
print(f"Cursor extablished in {e}ms")

s = t.time()
cur = con.cursor()
e = (t.time() - s)*1000
print(f"execute query in {e}ms")

s = t.time()
rows = cur.fetchmany(50)
e = (t.time() - s) * 1000
print(f"fetching first 50 rows in {e}ms")


cur.execute("select * from employees")
rows = cur.fetchmany(50)

cur.close()
con.close()
