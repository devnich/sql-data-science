# -----------------------------------------------
# Access database with built-in sqlite3 library
# -----------------------------------------------

import sqlite3

# Create a database connection
conn = sqlite3.connect("../data/portal_mammals.sqlite")

# Literal query
with conn:
    # Use a cursor to return query results
    c = conn.execute("SELECT * FROM surveys WHERE species_id = 'DM';")
    results = c.fetchall()
    c.close()

# Parameter substitution with unnamed parameters
with conn:
    query = "SELECT * FROM surveys WHERE species_id = ? AND year > ?;"
    args = ("DS", 1996)

    c = conn.execute(query, args)
    results = c.fetchall()

# Parameter substitution with named parameters; don't create intermediate
# cursor variable.
with conn:
    query_named = "SELECT * FROM surveys WHERE species_id = :id AND year > :year ORDER BY hindfoot_length;"
    args_named = {"id": "DM",
                  "year": 1995}

    results = conn.execute(query_named, args_named).fetchall()

# Iteration on results from implicit cursor
with conn:
    query = "SELECT * FROM surveys WHERE species_id = :id AND year > :year ORDER BY hindfoot_length;"
    args = {"id": "DS",
            "year": 1995}

    for row in conn.execute(query, args):
        print(row)


conn.close()

# -----------------------------------------------
# Access database with Pandas
# -----------------------------------------------

import pandas as pd
import sqlite3

# Create a database connection
conn = sqlite3.connect("../data/portal_mammals.sqlite")

query = "SELECT * FROM surveys WHERE species_id = :id AND year > :year ORDER BY hindfoot_length;"
args = {"id": "DS",
        "year": 1995}

df = pd.read_sql_query(query, conn, params=args)

conn.close()
