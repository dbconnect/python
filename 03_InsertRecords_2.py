import sqlite3

if __name__ == '__main__':
    print('Connecting to Database')
    conn = sqlite3.connect('student.db')
    print('Database Connected')

    print('Inserting Record (Better Way)')
    cur = conn.cursor()
    usn = '432'
    name = 'def'
    statement = "Insert Into student values(?, ?)"
    print(statement)
    cur.execute(statement, (usn, name))
    conn.commit()
    print('Record Inserted')

    conn.close()
