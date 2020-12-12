class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print("Наименование:", self._name, ", цена: ", self._price)


item = ItemDiscountReport("Книга", 500)
item.get_parent_data()
