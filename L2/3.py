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
        print("Наименование:", self.get_name(), ", цена: ", self.get_price())


item = ItemDiscountReport("Книга", 500)
item.get_parent_data()
