import sqlite3

if __name__ == '__main__':
    print('Connecting to Database')
    conn = sqlite3.connect('student.db')
    print('Database Connected')

    print('Inserting Record (Multiple Values)')
    cur = conn.cursor()
    statement = "Insert Into student values(?, ?)"
    data = [('714', 'rty'), ('129', 'zaq'), ('368', 'mju')]
    cur.executemany(statement, data)
    conn.commit()
    print('Record Inserted')

    conn.close()
