import psycopg2
from lagom.environment import Env

# Get parameters from ENV configuration
class DBConfig(Env):
    psql_user: str
    psql_pw: str
    psql_host: str
    psql_db: str
    psql_scheme: str

# def config_db(config: DBConfig):
def config_db():
    # 1. connect to database
    try:
        con = psycopg2.connect(
            host = "localhost",
            database = "apDB",
            user = "postgres",
            password="pw4asianpearl"
        )
    except Exception as error:
        print("not able to connec to the apDB")
        print("Oops! An exception has occured:", error)
        print ("Exception TYPE:", type(error))

    # 2. define a cursor to work with.
    cur = con.cursor()

    # 3. execute SQL query
    cur.execute("""SELECT * from products""")

    # 4. save the result
    data = cur.fetchall()

    # print data
    print("printing...", data)
    for item in data:
        print(item)
        print(f"0: {item[0]}, 1:{item[1]}")

    # close the cursor
    cur.close()

    # close the connection
    con.close()