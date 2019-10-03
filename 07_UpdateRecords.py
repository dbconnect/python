import sqlite3

if __name__ == '__main__':
    print('Connecting to Database')
    conn = sqlite3.connect('student.db')
    print('Database Connected')

    print('Updating Record')
    cur = conn.cursor()
    cur.execute("Update student SET name=? WHERE usn=?", ('qwe', '432'))
    print('Record Updated')
    conn.commit()

    conn.close()
