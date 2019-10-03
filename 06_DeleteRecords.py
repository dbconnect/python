import sqlite3

if __name__ == '__main__':
    print('Connecting to Database')
    conn = sqlite3.connect('student.db')
    print('Database Connected')

    print('Deleting Record')
    cur = conn.cursor()
    cur.execute("Delete From student where usn=?", ('123',))
    print('Record Deleted')
    conn.commit()

    conn.close()
