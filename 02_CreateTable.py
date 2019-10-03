import sqlite3

if __name__ == '__main__':
    print('Connecting to Database')
    conn = sqlite3.connect('student.db')
    print('Database Connected')

    print('Creating Student Table')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE student (usn text, name text)''')
    conn.commit()
    print('Student Table created and saved')

    conn.close()
