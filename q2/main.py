import json
import os


class UserManager:

    def __init__(self):
        self._users = []       # 按添加顺序保存用户列表
        self._next_id = 1      # 下一个待分配的id

    def add_user(self, name, age):
        """添加用户，自动分配id，返回该用户字典"""
        user = {"id": self._next_id, "name": name, "age": age}
        self._users.append(user)
        self._next_id += 1

        return user

    def get_user(self, user_id):
        """按id查询用户，不存在返回None"""
        for user in self._users:
            if user["id"] == user_id:
                return user

        return None

    def update_age(self, user_id, new_age):
        """修改指定用户的年龄，成功返回True，用户不存在返回False"""
        user = self.get_user(user_id)
        if user is None:
            return False
        user["age"] = new_age

        return True

    def remove_user(self, user_id):
        """删除指定用户，成功返回True，用户不存在返回False"""
        for i, user in enumerate(self._users):
            if user["id"] == user_id:
                self._users.pop(i)
                return True

        return False

    def list_users(self):
        """列出所有用户"""
        users = []
        for user in self._users:
            users.append(user)

        return users

    def save_to_json(self, filepath: str) -> None:
        """将所有用户保存为JSON"""
        data = {
            "next_id": self._next_id,
            "users": self._users,
        }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_from_json(self, filepath: str) -> None:
        """从 JSON 文件加载用户，覆盖当前数据。"""
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        self._users = data.get("users", [])
        self._next_id = data.get("next_id", 1)


if __name__ == "__main__":
    # 按照题目中的行为示例进行测试
    um = UserManager()

    print(um.add_user("张三", 18))   # {"id": 1, "name": "张三", "age": 18}
    print(um.add_user("李四", 20))   # {"id": 2, "name": "李四", "age": 20}
    print(um.get_user(1))            # {"id": 1, "name": "张三", "age": 18}
    print(um.get_user(99))           # None
    print(um.update_age(1, 19))      # True
    print(um.remove_user(2))         # True
    print(um.remove_user(2))         # False
    print(um.list_users())           # [{"id": 1, "name": "张三", "age": 19}]

    um.save_to_json("users.json")

    um2 = UserManager()
    um2.load_from_json("users.json")
    print(um2.list_users())          # [{"id": 1, "name": "张三", "age": 19}]

    u = um2.add_user("王五", 22)
    print(u)  # id 应为 3
