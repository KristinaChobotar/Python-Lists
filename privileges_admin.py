from users_on_the_site import User
#завдання с

class Admin(User):
    def __init__(self, first_name, last_name, age, country):
        super().__init__(first_name, last_name, age, country)
        self.priv = Privileges
#завдання d

class Privileges(Admin):
    def __init__(self,privileges):
        self.privileges = privileges

    def show_privileges(self):
        return f'Набір привелегій адміністратора: {self.privileges}.'

admin = Privileges('«Дозволено видаляти користувачів», «Дозволено блокувати користувачів»')
print(admin.show_privileges())