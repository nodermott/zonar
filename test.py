import unittest
from wishlist import app


class TestWishListTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000"
    USERS_URL = "{}/users".format(API_URL)
    BOOKS_URL = "{}/books".format(API_URL)
    WISHLIST_URL = "{}/wishlist".format(API_URL)

    # Test creating a user.
    def test_create_users(self):
        tester = app.test_client(self)
        r = tester.post("{}/{}".format(TestWishListTest.USERS_URL, "create?first_name=Bob&last_name=Test&email=bob"
                                                                   "@test.com&password=password"))
        self.assertTrue('New user created.', r.data)

    # Test finding all users.
    def test_findAll_users(self):
        tester = app.test_client(self)
        r = tester.get("{}/{}".format(TestWishListTest.USERS_URL, "all"))
        self.assertEqual(r.status_code, 200)

    # Test updating a user.
    def test_update_users(self):
        tester = app.test_client(self)
        r = tester.put("{}/{}".format(TestWishListTest.USERS_URL, "update?user_id=1&first_name=Bob&last_name=Test&"
                                                                  "email=bob@gmail.com&password=12345"))
        self.assertTrue('Updated user information.', r.data)

    # Test deleting a user.
    def test_delete_users(self):
        tester = app.test_client(self)
        r = tester.delete("{}/{}".format(TestWishListTest.USERS_URL, "delete?user_id=1"))
        self.assertTrue('User successfully deleted.', r.data)

    # Test creating a book.
    def test_create_books(self):
        tester = app.test_client(self)
        r = tester.post("{}/{}".format(TestWishListTest.BOOKS_URL, "create?title=Origin&author=Dan "
                                                                   "Brown&isbn=9789752123267&date_of_publication=10/3"
                                                                   "/2007"))
        self.assertTrue('New book created.', r.data)

    # Test finding all the books.
    def test_findAll_books(self):
        tester = app.test_client(self)
        r = tester.get("{}/{}".format(TestWishListTest.BOOKS_URL, "all"))
        self.assertEqual(r.status_code, 200)

    # Test updating a book.
    def test_update_books(self):
        tester = app.test_client(self)
        r = tester.put("{}/{}".format(TestWishListTest.BOOKS_URL, "update?title=Origin&author=Dan "
                                                                  "Brown&isbn=9780525434290&date_of_publication=10/3"
                                                                  "/2007"))
        self.assertTrue('Updated book information.', r.data)

    # Test deleting a book.
    def test_delete_books(self):
        tester = app.test_client(self)
        r = tester.delete("{}/{}".format(TestWishListTest.BOOKS_URL, "delete?book_id=1"))
        self.assertTrue('Book successfully deleted.', r.data)

    # Test adding a book to a users wish list.
    def test_create_wishlist(self):
        tester = app.test_client(self)
        r = tester.post("{}/{}".format(TestWishListTest.WISHLIST_URL, "create?user_id=1&book_id=1"))
        self.assertTrue('New book added to Wish List.', r.data)

    # Test finding all the wish lists.
    def test_findAll_wishlist(self):
        tester = app.test_client(self)
        r = tester.get("{}/{}".format(TestWishListTest.WISHLIST_URL, "all"))
        self.assertEqual(r.status_code, 200)

    # Test updating a users wish list.
    def test_update_wishlist(self):
        tester = app.test_client(self)
        r = tester.put("{}/{}".format(TestWishListTest.BOOKS_URL, "update?wishlist_id=1&user_id=1&book_id=2"))
        self.assertTrue('Wish List has been updated.', r.data)

    # Test deleting a book from the users wish list.
    def test_delete_wishlist(self):
        tester = app.test_client(self)
        r = tester.delete("{}/{}".format(TestWishListTest.WISHLIST_URL, "delete?wishlist_id=1"))
        self.assertTrue('Book has been removed from Wish List.', r.data)

    # Test finding the users wish list.
    def test_find_user_wishlist(self):
        tester = app.test_client(self)
        r = tester.get("{}/{}".format(TestWishListTest.WISHLIST_URL, "user?user_id=1"))
        self.assertEqual(r.status_code, 200)


if __name__ == "__main__":
    unittest.main()
