import requests


class AccountApi:
    def __init__(self, url: str = None, token: str = None):
        if url is None:
            self.url = "https://bookstore.toolsqa.com"
        else:
            self.url = url
        self.token = token
        self.headers = {
            'accept': 'application/json',
            'authorization': 'Basic b21lcm1hem9yMTI6T21lcjEyMyE==true',
            'Authorization': f'Bearer {self.token}'
        }

        self.session = requests.session()
        self.session.headers.update(self.headers)

    def post_authorized(self, login_view_model):
        login_view_model_data = login_view_model.to_json()
        res = self.session.post(url=f"{self.url}/Account/v1/Authorized", data=login_view_model_data)
        return res

    def post_generate_token(self, login_view_model):
        login_view_model_data = login_view_model.to_json()
        res = self.session.post(url=f"{self.url}/Account/v1/GenerateToken", data=login_view_model_data)
        return res

    def post_user(self, register_view_model):
        register_view_model_data = register_view_model.to_json()
        res = self.session.post(url=f"{self.url}/Account/v1/User", data=register_view_model_data)
        return res

    def delete_user_by_id(self, user_id: str):
        res = self.session.delete(url=f"{self.url}/Account/v1/User/{user_id}")
        return res

    def get_user_by_id(self, user_id: str):
        res = self.session.get(url=f"{self.url}/Account/v1/User/{user_id}")
        return res


class BookStoreApi:
    def __init__(self, url=None, token: str = None):
        if url is None:
            self.url = "https://bookstore.toolsqa.com"
        else:
            self.url = url
        self.token = token
        self.headrs = {
            'accept': 'application/json',
            'authorization': 'Basic b21lcm1hem9yMTI6T21lcjEyMyE==true',
            'Authorization': f'Bearer {self.token}'
        }
        self.session = requests.session()
        self.session.headers.update(self.headrs)

    def get_all_store_books(self):
        res = self.session.get(url=f"{self.url}/BookStore/v1/Books")
        return res

    def post_books(self, list_of_books):
        list_of_books_data = list_of_books.to_json()
        res = self.session.post(url=f"{self.url}/BookStore/v1/Books", data=list_of_books_data)
        return res

    def delete_books_by_userid(self, user_id: str):
        res = self.session.delete(url=f"{self.url}/BookStore/v1/Books?UserId={user_id}")
        return res

    def get_by_isbn(self, isbn: str):
        res = self.session.get(url=f"{self.url}/BookStore/v1/Book?ISBN={isbn}")
        return res

    def delete_books_by_string_object(self, string_object):
        string_object_data = string_object.to_json()
        res = self.session.delete(url=f"{self.url}/BookStore/v1/Book", data=string_object_data)
        return res

    def put_isbn(self, new_isbn: str, replace_isbn):
        replace_isbn_data = replace_isbn.to_json()
        res = self.session.put(url=f"{self.url}/BookStore/v1/Books/{new_isbn}", data=replace_isbn_data)
        return res



