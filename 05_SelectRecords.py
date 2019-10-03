import sqlite3

if __name__ == '__main__':
    print('Connecting to Database')
    conn = sqlite3.connect('student.db')
    print('Database Connected')

    print('Selecting Records')
    cur = conn.cursor()
    cur.execute("Select * From student")
    for row in cur:
        print(row)

    conn.close()
