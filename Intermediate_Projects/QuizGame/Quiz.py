class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("David", "N7")
user_2 = User("Alice", "B9")
print(user_1.user_id, user_1.name)
print(user_2.user_id, user_2.name)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
