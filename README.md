# Wish List Api

This is a wish list api to be able to add books to a users
wish list for future reading.

There are calls to find all, create, update, and delete users, books,
and wish list information.

## Here are some example calls

### Users Api Calls examples:

Find All Users: http://127.0.0.1:5000/users/all

Create User: http://127.0.0.1:5000/users/create?first_name=Bob&last_name=Test&email=bob@test.com&password=12345

Update User: http://127.0.0.1:5000/users/update?user_id=1&first_name=Bob&last_name=Test&email=bob@gmail.com&password=123456

Delete User: http://127.0.0.1:5000/users/delete?user_id=1

### Books Api Calls:

Find All Books: http://127.0.0.1:5000/books/all

Create Book: http://127.0.0.1:5000/books/create?title=Origin&author=Dan%20Brown&isbn=9789752123267&date_of_publication=10/3/2017

Update Book: http://127.0.0.1:5000/books/update?book_id=1?title=Origin&author=Dan%20Brown&isbn=9780525434290&date_of_publication=10/3/2017

Delete Book: http://127.0.0.1:5000/books/delete?book_id=1

### Wish List Api Calls:

Find All Wish Lists: http://127.0.0.1:5000/wishlist/all

Add a Book to Wish List: http://127.0.0.1:5000/wishlist/create?book_id=1&user_id=1

Update a Wish List: http://127.0.0.1:5000/wishlist/update?wishlist_id=1&book_id=1

Delete a Wish List: http://127.0.0.1:5000/wishlist/delete?wishlist_id=1

Find a users Wish List: http://127.0.0.1:5000/wishlist/user?user_id=1