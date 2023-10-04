import mysql.connector
mydb = mysql.connector.connect(host ='localhost', user = 'root', password = '', database = 'library')

if mydb.is_connected():
    print('Connection successful')

#search book  by author

def search_book():
    name = input('Enter author name :')
    conn = mydb.cursor()
    conn.execute("SELECT title FROM books WHERE author = %s", (name,))
    result = conn.fetchall()
    for i in result:
        print(i)
    return result


def add_book():
    btitle = input('Enter title: ')
    bauthor = input('Enter author name :')
    byear = input('Enter year: ')
    conn = mydb.cursor()
    result = conn.execute("INSERT INTO books (title, author, publication_year) VALUES (%s, %s, %s)",
            (btitle, bauthor, byear))
    mydb.commit()
    return result

add_book()
