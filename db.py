import psycopg2

# configuration for creating connection
pg_config = {
    'database': <database_name>,
    'host': '127.0.0.1',
    'user': <username>,
    'password': <password>,
    'port': '5432'
}

# creating table in db
def create():
    conn = psycopg2.connect(**pg_config)
    cur = conn.cursor()

    query = """create table if not exists testdetail (test_name varchar(255),test_desc varchar(255),test_report varchar(255),cost varchar(255));"""
    cur.execute(query)
    conn.commit()
    conn.close()
    cur.close()
  
# inserting data in to table
def insert(data): 
    query = """insert into testdetail(test_name,test_desc,test_report,cost)
                values(%s, %s, %s, %s);"""
    try: 
        # connect to the PostgreSQL database 
        conn = psycopg2.connect(**pg_config) 
        # create a new cursor 
        cur = conn.cursor() 

        # executing the INSERT statement 
        cur.execute(query, data) 
    
        # commit the changes to the database 
        conn.commit() 

        # close communication with the database 
        cur.close()  
    except (Exception, psycopg2.DatabaseError) as error: 
        print(error) 
    finally: 
        if conn is not None: 
            conn.close() 

# fetching data from db
def fetch(): 
    conn = psycopg2.connect(**pg_config) 
    cur = conn.cursor()
    cur.execute("select * from testdetail")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    cur.close()
    return rows

def deleteAll() : 
    conn = psycopg2.connect(**pg_config)
    cur = conn.cursor()
    cur.execute("delete from testdetail;")
    conn.commit()
    conn.close()
    cur.close()




