#завдання а
class Shop:
    def __init__(self, shop_name, store_type, number_of_units=0):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = number_of_units

    def describe_shop(self):
        return f'Магазин - {self.shop_name}, тип - {self.store_type}.'

    def open_shop(self):
        return 'Онлайн-магазин відкритий.'

    def set_number_of_units(self):
        return f'Кількість видів товару - {self.number_of_units}.'

    def increment_number_of_units(self, number):
        return self.number_of_units + number

store = Shop('Queen Store','магазин одягу')
print(store.shop_name)
print(store.store_type)
print(store.describe_shop())
print(store.open_shop())

#завдання b

store_jewelry = Shop('Silver country','ювелірний магазин')
print(store_jewelry.describe_shop())
store_makeup = Shop('Eva','магазин косметики')
print(store_makeup.describe_shop())
store_shoes = Shop('Центр-обувь','магазин взуття')
print(store_shoes.describe_shop())

#завдання с

print(store.number_of_units)
store.number_of_units = 1
print(store.number_of_units)

#завдання d

store.number_of_units = 5
print(store.set_number_of_units())
print(store.increment_number_of_units(5))

#завдання e

class Discount(Shop):
    def __init__(self,discount_products):
        self.discount_products = discount_products

    def get_discounts_products(self):
        return f'Список товарів, на які встановлена знижка: {self.discount_products}.'

store_discount = Discount('футболка, костюм')
print(store_discount.get_discounts_products())

