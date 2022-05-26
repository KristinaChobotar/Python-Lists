#завдання а
class User:
    login_attempts = 0
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country


    def describe_user(self):
        return f'Ім\'я користувача: {self.first_name} {self.last_name}.'

    def greeting_user(self):
        return f'Привіт, {self.first_name} {self.last_name}!'

    def increment_login_attempts(self):
        User.login_attempts += 1
        return User.login_attempts

    def reset_login_attempts(self):
        User.login_attempts = 0
        return User.login_attempts

Kristina = User('Христина', 'Чоботар', '17', 'Україна')
Angelina = User('Ангеліна', 'Сушинська', '18', 'Італія')
Michael = User('Майкл', 'Стоун', '20', 'Америка')
print(Kristina.describe_user())
print(Kristina.greeting_user())
print(Angelina.describe_user())
print(Angelina.greeting_user())
print(Michael.describe_user())
print(Michael.greeting_user())

#завдання b

print(Kristina.increment_login_attempts())
print(Angelina.increment_login_attempts())
print(Michael.increment_login_attempts())
print(Kristina.reset_login_attempts())
print(Angelina.reset_login_attempts())
print(Michael.reset_login_attempts())

#завдання с

class Admin(User):
    def __init__(self,privileges):
        self.privileges = privileges

    def show_privileges(self):
        return f'Набір привелегій адміністратора: {self.privileges}.'

admin = Admin('Дозволено видаляти користувачів, дозволено блокувати користувачів')
print(admin.show_privileges())

#завдання с

class Privileges(Admin):
    pass


