import sqlite3
conn = sqlite3.connect(':memory:')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS workers(
   workerid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   age INT,
   gender TEXT);
""")
conn.commit()
cur.execute("""CREATE TABLE IF NOT EXISTS salary(
   workerid INT PRIMARY KEY,
   salary amount INT,
   currency TEXT);
""")
conn.commit()
cur.execute("""CREATE TABLE IF NOT EXISTS position(
   workerid INT PRIMARY KEY,
   position TEXT,
   experience TEXT);
""")
conn.commit()
workers = [('001', 'Harry', 'Potter', '30', 'Male'), ('002', 'Ron', 'Wisley', '35', 'male')]
cur.executemany("INSERT INTO workers VALUES(?, ?, ?, ?, ?);", workers)
conn.commit()
salaries = [('001', '3000', 'USD'), ('002', '3500', 'EUR')]
cur.executemany("INSERT INTO salary VALUES(?, ?, ?);", salaries)
conn.commit()
positions = [('001', 'tester', '5 years'), ('002', 'programer', '6 years')]
cur.executemany("INSERT INTO position VALUES(?, ?, ?);", positions)
conn.commit()
cur.execute("SELECT * FROM workers;")
all_results = cur.fetchall()
print(all_results)
cur.execute("SELECT * FROM salary;")
all_results = cur.fetchall()
print(all_results)
cur.execute("SELECT * FROM position;")
all_results = cur.fetchall()
print(all_results)