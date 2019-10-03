import sqlite3

if __name__ == '__main__':
    print('Connecting to Database')
    conn = sqlite3.connect('student.db')
    print('Database Connected')

    print('Inserting Record (Insecure Way)')
    cur = conn.cursor()
    usn = '123'
    name = 'abc'
    statement = "Insert Into student values('{}', '{}')".format(usn, name)
    print(statement)
    cur.execute(statement)
    conn.commit()
    print('Record Inserted')

    conn.close()
