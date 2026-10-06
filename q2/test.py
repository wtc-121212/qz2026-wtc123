from main import UserManager


um = UserManager()

user1 = um.add_user("张三", 18)
user2 = um.add_user("李四", 20)

print(user1)
print(user2)

assert user1["id"] == 1
assert user2["id"] == 2

assert um.get_user(1)["name"] == "张三"
assert um.get_user(99) is None

assert um.update_age(1, 19) is True
assert um.get_user(1)["age"] == 19

assert um.update_age(99, 25) is False

assert um.remove_user(2) is True
assert um.remove_user(2) is False

print(um.list_users())

um.save_to_json("users.json")

um2 = UserManager()
um2.load_from_json("users.json")

print(um2.list_users())

user3 = um2.add_user("王五", 22)
assert user3["id"] == 2

print("全部测试通过")