import psycopg2
#connecting the database
con = psycopg2.connnect(
    host = "darigamac", 
    database = "darigadb",
    user = "pstgres", 
    password = "postgres", 
    port = 5432
)

cur = con.cursor()

#adding new data
cur.execute("insert into employees (id, name) values(%s, %s)", (1, "Hussein"))

#fetch from the query and return it, GIVE ME EVERYYYYYTHING TONIIIIIGHT
rows = cur.fetchall()

for r in rows:
    print(f"{r[0]} name {r[1]}")

#commit the changes
con.commit()

#always close the cursor, DONT LEAAK!!!
cur.close()

con.close()

