#cities.py
import sqlite3
conn=sqlite3.connect('getting_started.db')

with conn:
    c=conn.cursor()
    c.execute("DROP TABLE IF EXISTS cities")
    c.execute("CREATE TABLE cities(City TEXT, State TEXT)")
    c.execute("INSERT INTO cities VALUES('Boston', 'MA')")
    c.execute("INSERT INTO cities VALUES('New York', 'NY')")
    c.execute("INSERT INTO cities VALUES('Las Vegas', 'NV')")
    c.execute("SELECT * FROM cities")

    rows = c.fetchall()
    for row in rows:
        print row 



#weather.py
import sqlite3
conn=sqlite3.connect('getting_started.db')

with conn:
    c=conn.cursor()
    c.execute("DROP TABLE IF EXISTS weather")
    c.execute("CREATE TABLE weather(City TEXT, Year INT, Warmmonth TEXT, Coldmonth TEXT)")
    c.execute("INSERT INTO weather VALUES('Boston', '2013', 'July', 'January')")
    c.execute("INSERT INTO weather VALUES('New York', '2013', 'July', 'January')")
    c.execute("INSERT INTO weather VALUES('Las Vegas', '2013', 'July', 'January')")
    c.execute("SELECT * FROM weather")

    rows = c.fetchall()
    for row in rows:
        print row 


    #join.py
import sqlite3
conn=sqlite3.connect('getting_started.db')

with conn:
    c=conn.cursor()
    c.execute("SELECT * FROM cities");
    c.execute("SELECT * FROM weather");
    c.execute("SELECT * FROM cities, weather");

    rows = c.fetchall()
    for row in rows:
        print row   

    
    #pandastest.py
import sqlite3
import pandas as pd
conn=sqlite3.connect('getting_started.db')

with conn:
    c=conn.cursor()
    c.execute("SELECT * FROM weather")

    rows = c.fetchall()
    cols = [desc[0] for desc in c.description]
    df = pd.DataFrame(rows, columns=cols)
    print (df)


print "The city that is warmest in July is Las Vegas, NV."
    