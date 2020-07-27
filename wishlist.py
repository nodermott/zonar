"""
Nate Odermott
Zonar Wish List API coding exercise.
7/27/2020
filename: wishlist.py
"""

from flask import Flask, request, jsonify
import sqlite3
from inspect import getmembers
from pprint import pprint

app = Flask(__name__)


# function to return database results as a dictionary
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# Connect to to sqlite3 to create tables
conn = sqlite3.connect("TestDB.db")
cur = conn.cursor()
dropUserTable = "DROP TABLE if EXISTS users"
cur.execute(dropUserTable)
user_table = '''CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name varchar not null,
    last_name varchar not null,
    email varchar not null,
    password varchar not null
    )'''
cur.execute('DROP TABLE if EXISTS books')
book_table = '''CREATE TABLE books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title varchar not null,
    author varchar not null,
    isbn integer not null,
    date_of_publication text not null 
)'''
cur.execute('DROP TABLE if EXISTS wish_list')
wish_table = '''CREATE TABLE wish_list(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id integer not null,
    user_id varchar not null 
)'''
cur.execute(user_table)
print("users table created successfully.....")
cur.execute(book_table)
print("books table created successfully.....")
cur.execute(wish_table)
print("wish_list table created successfully.....")
conn.commit()
conn.close()


# Have a route to throw a 404 if incorrect url is supplied
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


# A route to return all of the available entries in our catalog.
@app.route('/users/all', methods=['GET'])
def api_all_users():
    conn = sqlite3.connect("TestDB.db")
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_users = cur.execute('SELECT * FROM users;').fetchall()
    conn.commit()
    conn.close()
    return jsonify("Users", all_users)


# A route to create users.
@app.route('/users/create', methods=['GET', 'POST'])
def api_create_users():
    if 'first_name' in request.args:
        first_name = str(request.args['first_name'])
    else:
        return "Error: No first_name field provided. Please specify an first_name."
    if 'last_name' in request.args:
        last_name = str(request.args['last_name'])
    else:
        return "Error: No last_name field provided. Please specify an last_name."
    if 'email' in request.args:
        email = str(request.args['email'])
    else:
        return "Error: No email field provided. Please specify an email."
    if 'password' in request.args:
        password = str(request.args['password'])
    else:
        return "Error: No password field provided. Please specify an password."
    conn = sqlite3.connect("TestDB.db")
    cur = conn.cursor()
    cur.execute('INSERT INTO users(first_name, last_name, email, password) values (?, ?, ?, ?)',
                (first_name, last_name, email, password))
    conn.commit()
    conn.close()

    return 'New user created.'


# a route to update a user.  Supply the user_id and the user information including the updated info.
@app.route('/users/update', methods=['GET', 'PUT'])
def api_update_users():
    pprint(getmembers(request))
    if 'user_id' in request.args:
        user_id = int(request.args['user_id'])
    else:
        return "Error: No user_id field provided. Please specify an user_id."
    if 'first_name' in request.args:
        first_name = str(request.args['first_name'])
    else:
        return "Error: No first_name field provided. Please specify an first_name."
    if 'last_name' in request.args:
        last_name = str(request.args['last_name'])
    else:
        return "Error: No last_name field provided. Please specify an last_name."
    if 'email' in request.args:
        email = str(request.args['email'])
    else:
        return "Error: No email field provided. Please specify an email."
    if 'password' in request.args:
        password = str(request.args['password'])
    else:
        return "Error: No password field provided. Please specify an password."

    conn = sqlite3.connect("TestDB.db")
    cur = conn.cursor()
    cur.execute('''UPDATE users set first_name = ?, last_name = ?, email = ?, password = ? WHERE id = ?''',
                (first_name, last_name, email, password, user_id))
    conn.commit()
    conn.close()
    return 'Updated user information.'


# A route to delete a user.  Delete user by the user_id.
@app.route('/users/delete', methods=['GET', 'POST'])
def api_delete_users():
    if 'user_id' in request.args:
        user_id = str(request.args['user_id'])
    else:
        return "Error: No user_id field provided. Please specify an user_id."

    conn = sqlite3.connect("TestDB.db")
    cur = conn.cursor()
    cur.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()

    return 'User successfully deleted.'


# A route to return all of the available entries of books in our catalog.
@app.route('/books/all', methods=['GET'])
def api_all_books():
    conn = sqlite3.connect("TestDB.db")
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM books;').fetchall()
    conn.commit()
    conn.close()
    return jsonify('Books', all_books)


# A route to create books.
@app.route('/books/create', methods=['GET', 'POST'])
def api_create_books():
    if 'title' in request.args:
        title = str(request.args['title'])
    else:
        return "Error: No title field provided. Please specify an title."
    if 'author' in request.args:
        author = str(request.args['author'])
    else:
        return "Error: No author field provided. Please specify an author."
    if 'isbn' in request.args:
        isbn = str(request.args['isbn'])
    else:
        return "Error: No isbn field provided. Please specify an isbn."
    if 'date_of_publication' in request.args:
        date_of_publication = str(request.args['date_of_publication'])
    else:
        return "Error: No date field provided. Please specify an date."
    conn = sqlite3.connect("TestDB.db")
    cur = conn.cursor()
    cur.execute('INSERT INTO books(title, author, isbn, date_of_publication) values (?, ?, ?, ?)',
                (title, author, isbn, date_of_publication))
    conn.commit()
    conn.close()

    return 'New book created.'


# A route to update book information.
@app.route('/books/update', methods=['GET', 'PUT'])
def api_update_books():
    if 'book_id' in request.args:
        book_id = str(request.args['book_id'])
    else:
        return "Error: No book_id field provided. Please specify an book_id."
    if 'title' in request.args:
        title = str(request.args['title'])
    else:
        return "Error: No title field provided. Please specify an title."
    if 'author' in request.args:
        author = str(request.args['author'])
    else:
        return "Error: No author field provided. Please specify an author."
    if 'isbn' in request.args:
        isbn = str(request.args['isbn'])
    else:
        return "Error: No isbn field provided. Please specify an isbn."
    if 'date_of_publication' in request.args:
        date_of_publication = str(request.args['date_of_publication'])
    else:
        return "Error: No date field provided. Please specify an date."
    conn = sqlite3.connect("TestDB.db")
    cur = conn.cursor()
    cur.execute('UPDATE books SET title = ?, author = ?, isbn = ?, date_of_publication = ? WHERE id = ?',
                (title, author, isbn, date_of_publication, book_id))
    conn.commit()
    conn.close()
    return 'Updated book information.'


# A route to delete a book.  Delete a book buy the book_id.
@app.route('/books/delete', methods=['GET', 'DELETE'])
def api_delete_books():
    if 'book_id' in request.args:
        book_id = str(request.args['book_id'])
    else:
        return "Error: No book_id field provided. Please specify an book_id."
    conn = sqlite3.connect("TestDB.db")
    cur = conn.cursor()
    cur.execute('''DELETE FROM books WHERE id = ?''', (book_id,))
    conn.commit()
    conn.close()
    return 'Book has been deleted'


# A route to return all of the available wish list entries in our catalog.
@app.route('/wishlist/all', methods=['GET'])
def api_all_wishlist():
    conn = sqlite3.connect("TestDB.db")
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('''SELECT * FROM wish_list''').fetchall()
    conn.commit()
    conn.close()
    return jsonify('Wish List', all_books)


# A route to return all books in the users wish list.
@app.route('/wishlist/user', methods=["GET"])
def api_user_wishlist():
    if 'user_id' in request.args:
        user_id = str(request.args['user_id'])
    else:
        return "Error: No id field provided. Please specify an id."
    conn = sqlite3.connect("TestDB.db")
    conn.row_factory = dict_factory
    cur = conn.cursor()
    wishlist = cur.execute('''SELECT b.* FROM books b INNER JOIN wish_list wl on wl.book_id = b.id WHERE wl.user_id = ?''', (user_id,)).fetchall()
    conn.commit()
    conn.close()
    return jsonify('Wish List', wishlist)


# A route to add a book to the users wish list.
@app.route('/wishlist/create', methods=["GET", "POST"])
def api_create_wishlist():
    if 'user_id' in request.args:
        user_id = str(request.args['user_id'])
    else:
        return "Error: No user_id field provided. Please specify a user_id."
    if 'book_id' in request.args:
        book_id = str(request.args['book_id'])
    else:
        return "Error: No book_id field provided. Please specify an book_id."
    conn = sqlite3.connect("TestDB.db")
    cur = conn.cursor()
    cur.execute('''INSERT INTO wish_list(book_id, user_id) values (?, ?)''',
                (book_id, user_id))
    conn.commit()
    conn.close()

    return 'New book added to Wish List.'


# A route to update a users wish list.
@app.route('/wishlist/update', methods=['GET', 'PUT'])
def api_update_wishlist():
    if 'wishlist_id' in request.args:
        wishlist_id = str(request.args['wishlist_id'])
    else:
        return "Error: No wishlist_id field provided. Please specify a wishlist_id."
    if 'user_id' in request.args:
        user_id = str(request.args['user_id'])
    else:
        return "Error: No user_id field provided. Please specify a user_id."
    if 'book_id' in request.args:
        book_id = str(request.args['book_id'])
    else:
        return "Error: No book_id field provided. Please specify an book_id."
    conn = sqlite3.connect("TestDB.db")
    cur = conn.cursor()
    cur.execute('''UPDATE wish_list set book_id = ?, user_id = ? WHERE id = ?''',
                (book_id, user_id, wishlist_id))
    conn.commit()
    conn.close()

    return 'Wish List has been updated.'


# A route to delete a book off of the users wishlist.
@app.route('/wishlist/delete', methods=['GET', 'DELETE'])
def api_delete_wishlist():
    if 'wishlist_id' in request.args:
        wishlist_id = str(request.args['wishlist_id'])
    else:
        return "Error: No wishlist_id field provided. Please specify an wishlist_id."
    conn = sqlite3.connect("TestDB.db")
    cur = conn.cursor()
    cur.execute('''DELETE FROM wish_list WHERE id = ''',
                (wishlist_id,))
    conn.commit()
    conn.close()

    return 'Book has been removed from Wish List.'


app.run()
