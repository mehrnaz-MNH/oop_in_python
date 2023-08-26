import csv
class Item :
    pay_rate = 0.8 # class attribute
    all_items = []
    # every time an object is made , the constructor gets called
    def __init__(self , name:str, price:float , quantity = 0 ) :

        # run validation
        assert price >= 0 ,f"the {price} is not greater than 0 "
        assert quantity >= 0,f"the {quantity} is not greater than 0 "
        # assign value to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        # actions to execute
        Item.all_items.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as file :
            reader = csv.DictReader(file)
            items = list(reader)

        for item in items :
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity =int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        pass

    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self) :
        return  f"Item( '{self.name}' , '{self.price}' , '{self.quantity}' )"


# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

Item.instantiate_from_csv()

print(Item.all_items)

# for instance in Item.all_items :
#     print(instance.name)

