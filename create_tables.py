import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """
    - Creates and connects to the sparkifydb
    - Returns the connection and cursor to sparkifydb
    """
    
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    drop_table_queries = []
    
    # songplays table
    drop_table_queries.append("DROP TABLE IF EXISTS songplays")
    
    # users table
    drop_table_queries.append("DROP TABLE IF EXISTS users")
    
    # songs table
    drop_table_queries.append("DROP TABLE IF EXISTS songs")
    
    # artists table
    drop_table_queries.append("DROP TABLE IF EXISTS artists")
    
    # time table
    drop_table_queries.append("DROP TABLE IF EXISTS time")
    
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()
        


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    create_table_queries = []
    
    # songplays table
    create_table_queries.append("CREATE TABLE songplays (\
        songplay_id int PRIMARY KEY, \
        start_time timestamp, \
        user_id varchar, \
        level varchar NOT NULL, \
        song_id varchar NOT NULL, \
        artist_id varchar NOT NULL, \
        session_id int NOT NULL, \
        location varchar, \
        user_agent varchar)")
    
    # users table
    create_table_queries.append("CREATE TABLE users (\
        user_id varchar PRIMARY KEY, \
        first_name varchar NOT NULL, \
        last_name varchar NOT NULL, \
        gender varchar(1) NOT NULL, \
        level varchar NOT NULL)")
    
    # songs table
    create_table_queries.append("CREATE TABLE songs (\
        song_id varchar PRIMARY KEY, \
        title varchar NOT NULL, \
        artist_id varchar NOT NULL, \
        year int, \
        duration decimal)")
    
    # artists table
    create_table_queries.append("CREATE TABLE artists (\
        artist_id varchar PRIMARY KEY, \
        name varchar NOT NULL, \
        location varchar, \
        latitude decimal, \
        longitude decimal)")
    
    # time table
    create_table_queries.append("CREATE TABLE time (\
        start_time timestamp PRIMARY KEY, \
        hour int, \
        day int, \
        weekofyear int, \
        month int, \
        year int, \
        weekday int)")
    
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Drops (if exists) and Creates the sparkify database. 
    
    - Establishes connection with the sparkify database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    
    
    
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()
    
    
    

if __name__ == "__main__":
    main()