class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class ItemDiscountReportOne(ItemDiscount):
    def get_parent_data(self):
        print("Наименование:", self.get_name(), ", цена со скидкой:",
              self.calc_discount(self._ItemDiscount__price, self.discount))

    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        return '({}, {})'.format(self._ItemDiscount__name, self.calc_discount(self._ItemDiscount__price, self.discount))

    def calc_discount(self, price, discount):
        return price - price / 100 * discount

    def get_info(self):
        print("ClassOne. Наименование:", self.get_name(), ", цена:", self.get_price())


class ItemDiscountReportTwo(ItemDiscount):
    def get_parent_data(self):
        print("Наименование:", self.get_name(), ", цена со скидкой:",
              self.calc_discount(self._ItemDiscount__price, self.discount))

    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        return '({}, {})'.format(self._ItemDiscount__name, self.calc_discount(self._ItemDiscount__price, self.discount))

    def calc_discount(self, price, discount):
        return price - price / 100 * discount

    def get_info(self):
        print("ClassTwo. Наименование:", self.get_name(), ", цена:", self.get_price())


item1 = ItemDiscountReportOne("Книга", 500, 10)
item2 = ItemDiscountReportTwo("Книга", 500, 10)
item1.get_info()
item2.get_info()

for ob in (item1, item2):
    ob.get_info()


def pol_function(ob):
    ob.get_info()


pol_function(item1)
pol_function(item2)
