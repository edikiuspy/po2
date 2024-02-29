import po2.src.structure as structure


class Logic:
    def __init__(self):
        self.users = []

    def get_users(self):
        return self.users

    def add_user(self, user):
        user = structure.User(**user,id=len(self.users)+1)
        self.users.append(user.dict())

    def get_user(self, user_id):
        for user in self.users:
            if user['id'] == user_id:
                return user
        return None

    def update_user(self, user_id, user):
        for i in range(len(self.users)):
            if self.users[i]['id'] == user_id:
                self.users[i] = structure.User(**user,id=user_id).dict()
                return

    def delete_user(self, user_id):
        for i in range(len(self.users)):
            if self.users[i]['id'] == user_id:
                del self.users[i]
                return

    def validate_user(self, user):
        try:
            structure.User(**user)
            return True
        except structure.pydantic.ValidationError:
            return False
