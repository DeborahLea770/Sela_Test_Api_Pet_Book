import pytest
from models.book_model import Book
from models.login_view_model import LoginViewModel
from models.register_view_model import RegisterView
from models.collection_of_isbn import CollectionOfIsbn
from models.add_list_of_books import AddListBooks
from models.create_user_result import CreateUserResult
from models.get_user_result import GetUserResult
from models.replace_isbn import ReplaceIsbn
from models.string_object import StringObject
from api.account_api import AccountApi
from api.book_store_api import BookStoreApi
import  logging
import datetime


user_ID = open("models/id.txt", "r")
token = open("models/token.txt", "r")
userIDR = user_ID.read()
tokenR = token.read()
accountApi = AccountApi("https://bookstore.toolsqa.com", )
bookStoreApi = BookStoreApi("https://bookstore.toolsqa.com")
bookStoreApiToken = BookStoreApi("https://bookstore.toolsqa.com", tokenR)
accountApiToken = AccountApi("https://bookstore.toolsqa.com")
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)
mylogger = logging.getLogger()

@pytest.fixture()
def My_Details() -> RegisterView:
    register_view = RegisterView("deborah770", "Deborah@770")
    return register_view


@pytest.fixture()
def My_User() -> LoginViewModel:
    login_view = LoginViewModel("deborah770", "Deborah@770")
    return login_view


@pytest.fixture()
def My_List_Of_Books() -> AddListBooks:
    C = CollectionOfIsbn("111111111")
    addListOfBooks = AddListBooks(userIDR, [C])
    return addListOfBooks


@pytest.fixture()
def My_Book() -> Book:
    book = Book("1234", "flower", "Store Flower",
                "deb fellous", datetime.datetime(2012, 26, 5), "paris", 566, "teva",
                "https://www.flower.com/")
    return book


@pytest.fixture()
def My_String_Object() -> StringObject:
    user_ID = open("models/id.txt", "r")
    string_object = StringObject("928492034182304", user_ID.read())
    return string_object


@pytest.fixture()
def My_Replace_Isbn() -> ReplaceIsbn:
    userID = open("models/id.txt", "r")
    replace_isbn = ReplaceIsbn(userID.read(), "gdghfyjfyggdsdytfj")
    return replace_isbn


def test_post_user(My_Details, My_User):
    mylogger.info("test for create new user")
    res_post_user = accountApi.post_user(My_Details)
    assert res_post_user.status_code == 201
    assert res_post_user.json()["username"] == My_Details.userName
    user_ID = open("../Book2/models/id.txt", "w")
    token = open("../Book2/models/token.txt", "w")
    user_ID.write(res_post_user.json()["userID"])
    res_post_token = accountApi.post_generate_token(My_User)
    token.write(res_post_token.json()["token"])


def test_post_authorized(My_User):
    mylogger.info("test for user authorization")
    res_post = accountApiToken.post_authorized(My_User)
    assert res_post.status_code == 200
    assert res_post.json() is True


def test_post_generate_token(My_User):
    mylogger.info("test for generate new token")
    res_post = accountApi.post_generate_token(My_User)
    assert res_post.status_code == 200
    token = open("../Book2/models/token.txt", "w")
    token.seek(0)
    token.write(res_post.json()["token"])


def test_get_user_by_id():
    mylogger.info("test for get user by id")
    res_get = accountApiToken.get_user_by_id(userIDR)
    assert res_get.status_code == 200
    mylogger.info(res_get.json()['userId'])


def test_delete_user_by_id():
    mylogger.info("test for delete user by id")
    res_delete = accountApiToken.delete_user_by_id(userIDR)
    assert res_delete.status_code == 204
    res_get = accountApiToken.get_user_by_id(userIDR)
    assert res_get.status_code == 401


def test_get_all_store_books():
    mylogger.info("test for get all books in the store")
    res_get = bookStoreApi.get_all_store_books()
    assert res_get.status_code == 200
    mylogger.info(res_get.json())


def test_post_books(My_List_Of_Books):
    mylogger.info("test for create list of books")
    mylogger.error("this test getting error 504-Gateway Time-Out everytime!!!")
    res_delete = bookStoreApiToken.delete_books_by_userid(userIDR)
    assert res_delete.status_code == 204
    res_post = bookStoreApiToken.post_books(My_List_Of_Books[0])
    assert res_post.status_code == 504
    mylogger.error("504 Gateway Time-out")
    assert res_post.status_code == 201
    mylogger.info(f"Success! {res_post.json()}")


def test_delete_books_by_userid():
    res_delete = bookStoreApiToken.delete_books_by_userid(userIDR)
    assert res_delete.status_code == 204
    mylogger.info(res_delete.text)


def test_get_by_isbn():
    mylogger.info("test for get books by isbn")
    res_get = bookStoreApi.get_all_store_books()
    assert res_get.status_code == 200
    assert res_get.json()["books"][0]["isbn"]
    res_get2 = bookStoreApi.get_by_isbn(res_get.json()["books"][0]["isbn"])
    assert res_get2.status_code == 200
    assert res_get2.json()["isbn"] == res_get.json()["books"][0]["isbn"]


def test_delete_books_by_string_object(My_List_Of_Books,My_String_Object):
    mylogger.info("test for delete books by string object (isbn, userid)")
    res_get = accountApiToken.get_user_by_id(userIDR)
    assert res_get.status_code == 200
    res_post = bookStoreApiToken.post_books(My_List_Of_Books)
    assert res_post.status_code == 201
    res_delete = bookStoreApiToken.delete_books_by_string_object(My_String_Object)
    res_get2 = accountApiToken.get_user_by_id(userIDR)
    assert res_delete.status_code == 204
    mylogger.info("book deleted successfully!")
    books_before = res_get.json()["books"]
    books_after = res_get2.json()["books"]
    assert len(books_after) < len(books_before)


def test_put_isbn(My_List_Of_Books,My_String_Object,My_Replace_Isbn):
    mylogger.info("test for change isbn of user's book list")
    res_post = bookStoreApiToken.post_books(My_List_Of_Books)
    assert res_post.status_code == 201
    res_get = accountApiToken.get_user_by_id(userIDR)
    assert res_get.status_code == 200
    books = res_get.json()["books"]
    res_put = bookStoreApi.put_isbn(books[0]["isbn"], My_Replace_Isbn)
    assert res_put.status_code == 200
    assert res_put.json()["books"][0]["isbn"] == My_Replace_Isbn.isbn

