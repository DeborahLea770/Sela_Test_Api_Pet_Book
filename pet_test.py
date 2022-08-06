import pytest
from models.pet import Pet
from models.category import Category
from models.tags import Tags
from models.order import Order
from models.user import User
import api.pet_api as pet_api
import api.order_api as order_api
import api.user_api as user_api
import datetime
import json
import logging
logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()

petApi = pet_api.PetApi("https://petstore3.swagger.io/api/v3")
orderApi = order_api.OrderApi("https://petstore3.swagger.io/api/v3/store")
userApi = user_api.UserApi("https://petstore3.swagger.io/api/v3/user")


@pytest.fixture()
def MPet() -> Pet:
    category = Category(234, "Cat")
    photoUrls = ["https://en.wikipedia.org/wiki/Cat#/media/File:Cat_poster_1.jpg"]
    tags = [Tags(3453445, "tag1")]
    mitzi = Pet(20, "mitzi", category, photoUrls, tags, "available")
    return mitzi


@pytest.fixture()
def MOrder() -> Order:
    my_order = Order(3242, 3424, 1, datetime.datetime.now(), "placed", False)
    return my_order


@pytest.fixture()
def MUser() -> User:
    my_user = User(32435, "Deb", "2wfs324", "Deb", "Fel", "deborahlea770@gmail.com", 345678976, 5)
    return my_user


@pytest.fixture()
def MUsers() -> [User]:
    U1 = User(12232, "tal", "2wfs324", "tal", "tal", "tal@gmail.com", 234152433, 5)
    U2 = User(32454, "dan", "2wfs324", "dan", "dan", "dan@gmail.com", 836452872, 5)
    users = [U1, U2]
    return users


def test_put_pet(MPet):
    mylogger.info("test for put pet")
    re = petApi.post_new_pet(MPet)
    print(re.url)
    MPet.name = "Deb"
    res_put = petApi.put_pet(MPet)
    res_get = petApi.get_pet_by_id(MPet.id)
    assert res_put.status_code == 200
    assert MPet.name == res_get.json()["name"]


def test_post_new_pet(MPet):
    mylogger.info("test for post new pet")
    res_delete = petApi.delete_pet_by_id(MPet.id)
    res_post = petApi.post_new_pet(MPet)
    assert res_post.status_code == 200
    res_get = petApi.get_pet_by_id(MPet.id)
    assert res_get.status_code == 200
    assert res_get.json() == res_post.json()


def test_get_pet_byid(MPet):
    mylogger.info("test for get pet by id")
    petApi.post_new_pet(MPet)
    res_get = petApi.get_pet_by_id(MPet.id)
    assert res_get.status_code == 200
    assert res_get.json()["id"] == MPet.id


def test_get_pets_bystatus(MPet):
    mylogger.info("test for get pet by status")
    res_get = petApi.get_pets_by_status(MPet.status)
    assert res_get.status_code == 200
    statusArray = []
    for pet in res_get.json():
        statusArray.append(pet["status"])
    assert MPet.status in statusArray


def test_get_pet_bytags(MPet):
    mylogger.info("test for get pet by tags")
    tags = []
    print(MPet.tags[0].name)
    for tag in MPet.tags:
        print(tag.name)
        tags.append(tag.name)
    res_get = petApi.get_pet_by_tags(tags)
    assert res_get.status_code == 200
    tagsNames = []
    for pet in res_get.json():
        for tag in pet["tags"]:
            if isinstance(tag, dict):
                tagsNames.append(tag["name"])
    assert MPet.tags[0].name in tagsNames


def test_post_pet_byid_and_update(MPet):
    mylogger.info("test for post pet by id and update")
    petApi.post_new_pet(MPet)
    pet_before = [MPet.name, MPet.status]
    MPet.name = "dany"
    MPet.status = "sold"
    pet_after = [MPet.name, MPet.status]
    res_post = petApi.post_pet_by_id_and_update(MPet.id, MPet.name, MPet.status)
    assert res_post.status_code == 200
    assert res_post.json()["name"] != pet_before[0] and res_post.json()["status"] != pet_before[1]
    assert res_post.json()["name"] == pet_after[0] and res_post.json()["status"] == pet_after[1]


def test_delete_pet_byid(MPet):
    mylogger.info("test for delete pet by id")
    res_post = petApi.post_new_pet(MPet)
    assert res_post.status_code == 200
    res_delete = petApi.delete_pet_by_id(MPet.id)
    assert res_delete.status_code == 200
    res_get = petApi.get_pet_by_id(MPet.id)
    assert res_get.status_code == 404


def test_upload_image_byid(MPet):
    mylogger.info("test for upload image by id")
    files = {'upload_file': open('slide-1.jpg', 'rb')}
    res_post = petApi.upload_image_by_id(MPet.id, files)
    assert res_post.status_code == 200
    print(res_post.json()["message"])


def test_get_store_inventory():
    mylogger.info("test for get store inventory")
    res_get = orderApi.get_store_inventory()
    assert res_get.status_code == 200
    assert type(res_get.json()) == dict


def test_post_order(MOrder):
    mylogger.info("test for post order")
    orderApi.delete_order(MOrder.id)
    res_post = orderApi.post_order(MOrder)
    assert res_post.status_code == 200
    res_get = orderApi.get_order(MOrder.id)
    print(res_get.json())
    assert res_get.status_code == 200
    assert res_get.json() == res_post.json()


def test_get_order(MOrder):
    mylogger.info("test for get order")
    res_get = orderApi.get_order(MOrder.id)
    assert res_get.status_code == 200
    assert res_get.json()["id"] == MOrder.id


def test_delete_order(MOrder):
    mylogger.info("test for delete order")
    res_post = orderApi.post_order(MOrder)
    assert res_post.status_code == 200
    res_delete = orderApi.delete_order(MOrder.id)
    assert res_delete.status_code == 200
    res_get = orderApi.get_order(MOrder.id)
    assert res_get.status_code == 404


def test_post_user(MUser):
    mylogger.info("test for post user")
    userApi.delete_username(MUser.username)
    res_post = userApi.post_user(MUser)
    assert res_post.status_code == 200
    res_get = userApi.get_username(MUser.username)
    assert res_get.status_code == 200
    assert res_get.json() == res_post.json()


def test_post_users(MUsers):
   mylogger.info("test for create a list of new users")
    mylogger.info("test post users")
    mylogger.error("this test getting error!!!")
    users = [user.to_json() for user in MUsers]
    users_json = json.dumps(users)
    res_post = userApi.post_users_list(users_json)
    assert res_post.status_code == 200


def test_get_login(MUser):
    mylogger.info("test for get login")
    print(user_api.UserApi()._url)
    res_get = user_api.UserApi().get_login(MUser.username, MUser.password)
    assert res_get.status_code == 200
    print(res_get.content)


def test_get_logout():
    mylogger.info("test for get logout")
    res_get = user_api.UserApi().get_logout()
    assert res_get.status_code == 200
    print(res_get.content)


def test_get_username(MUser):
    mylogger.info("test for get username")
    res_post = userApi.post_user(MUser)
    assert res_post.status_code == 200
    res_get = userApi.get_username(MUser.username)
    assert res_get.status_code == 200
    assert res_get.json()["username"] == MUser.username


def test_put_username(MUser):
    mylogger.info("test for put username")
    res_post = userApi.post_user(MUser)
    assert res_post.status_code == 200
    MUser.username = "tamar"
    res_put = userApi.put_username(MUser)
    assert res_put.json()["name"] == MUser.username


def test_delete_username(MUser):
    mylogger.info("test for delete username")
    res_post = userApi.post_user(MUser)
    assert res_post.status_code == 200
    res_delete = userApi.delete_username(MUser.username)
    assert res_delete.status_code == 200
    res_get = userApi.get_username(MUser.username)
    assert res_get.status_code == 404
