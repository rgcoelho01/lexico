import psycopg2 as p

conn = None
cur = None
try:
    conn = p.connect("dbname='teste' user='postgres' password='postgres'")
    cur = conn.cursor()
except (Exception, p.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
