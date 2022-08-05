import requests


class AccountApi:
    def __init__(self, url=None):
        if url is None:
            self.url = "https://bookstore.toolsqa.com"
        else:
            self.url = url
        self.headrs = {'accept': 'application/json'}
        self.session = requests.session()
        self.session.headers.update(self.headrs)

    def post_authorized(self, login_view):
        login_view_d = login_view.to_json()
        res = self.session.post(url=f"{self.url}/Account/v1/Authorized", data=login_view_d)
        return res

    def post_generate_token(self, login_view):
        login_view_d = login_view.to_json()
        res = self.session.post(url=f"{self.url}/Account/v1/GenerateToken", data=login_view_d)
        return res

    def post_user(self, register_view):
        register_view_d = register_view.to_json()
        res = self.session.post(url=f"{self.url}/Account/v1/User", data=register_view_d)
        return res

    def delete_user_by_id(self, user_id: str):
        res = self.session.delete(url=f"{self.url}/Account/v1/User/{user_id}")
        return res

    def get_user_by_id(self, user_id: str):
        res = self.session.get(url=f"{self.url}/Account/v1/User/{user_id}")
        return res


