import sqlite3

if __name__ == '__main__':
    print('Connecting to Database')
    conn = sqlite3.connect('student.db')
    print('Connected to Database')
    conn.close()
