class ItemDiscount:
    def __init__(self, name, price):
        self._name = name
        self._price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print("Наименование:", self._name, ", цена: ", self._price)


item = ItemDiscountReport("Книга", 500)
item.get_parent_data()
