class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print("наименование:", self.get_name(), ", цена со скидкой: ",
              self.calc_discount(self._ItemDiscount__price, self.discount))

    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        return '({}, {})'.format(self._ItemDiscount__name, self.calc_discount(self._ItemDiscount__price, self.discount))

    def calc_discount(self, price, discount):
        return price - price / 100 * discount


item = ItemDiscountReport("Книга", 500, 10)
item.get_parent_data()
print(item)
