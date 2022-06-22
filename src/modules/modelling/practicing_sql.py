import psycopg2
import psycopg2.extras
import json
import sys
sys.path.insert(0, '/Users/akankshav/Documents/Holmusk/GitRepos/demo_holmusk/src/')
from lib.resultGraph import myplotter


info = json.load(open("/Users/akankshav/Documents/Holmusk/GitRepos/demo_holmusk/config/config.json"))
hostname = info['postgres']['hostname']
database = info['postgres']['database']
username = info['postgres']['username']
password = info['postgres']['password']
port = info['postgres']['port']
conn = None
cur = None

def printrows(fetchall):
    print("--"*20)
    for row in fetchall:
        print(row)

try:
    conn = psycopg2.connect(host=hostname, dbname=database, user=username, password=password, port=port)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # num = int(input("Enter which example to execute:"))
    num = 5
    if(num == 1):
        cur.execute("select table_name from information_schema.tables where table_schema = 'public'")
        printrows(cur.fetchall()) 
    elif(num ==2):
        cur.execute("select first_name , last_name from actor limit 10")
        printrows(cur.fetchall()) 
    elif(num ==3):
        cur.execute("select * from film limit 10")
        printrows(cur.fetchall()) 
    elif(num ==4):
        cur.execute("select * from film")
        printrows(cur.fetchall()) 
    elif(num==5):
        cur.execute("select first_name , count(1) as freq from actor group by first_name order by freq desc")
        # print(cur.fetchall())
        keys = []
        values = []
        limit = 30
        for record in cur.fetchall():
            keys.append(record[0])
            values.append(record[1])
        
        myplotter.freq_plot(keys[:limit], values[:limit],'first_names')
    elif(num == 6):
        cur.execute("copy film to '/Users/akankshav/Documents/Holmusk/GitRepos/demo_holmusk/results/output.csv' delimiter ';' csv")
        # cur.execute("copy film to '/tmp/output.csv' delimiter ';' csv")
        # filepath = '/tmp/output.csv'
        # print("csv file has been saved to ",filepath)

    conn.commit()
except Exception as e:
    print(e)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:    
        conn.close()