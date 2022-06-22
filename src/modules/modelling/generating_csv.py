from curses.ascii import US
import psycopg2
import psycopg2.extras
import json
import sys

sys.path.insert(0,'/Users/akankshav/Documents/Holmusk/GitRepos/demo_holmusk/src/')
info  = json.load(open("/Users/akankshav/Documents/Holmusk/GitRepos/demo_holmusk/config/db.json"))

conn = None
cur = None

try :
    conn = psycopg2.connect(info['dvdrental']['connection'])
    cur = conn.cursor()
    cur.execute("copy film to '/Users/akankshav/Documents/Holmusk/GitRepos/demo_holmusk/results/output2.csv' delimiter ';' csv")
    print("Successfully copied film to '/results/output2.csv'")
except Exception as e:
    print(e)

finally:
    if cur is not None:
        cur.close()
    if conn is not None :
        conn.close()