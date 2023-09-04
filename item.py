import csv
class Item :
    pay_rate = 0.8 # class attribute
    all_items = [] #class attribute
    # every time an object is made , the constructor gets called
    def __init__(self , name:str, price:float , quantity = 0 ) : # constructor

        # run validation
        assert price >= 0 ,f"the {price} is not greater than 0 "
        assert quantity >= 0,f"the {quantity} is not greater than 0 "
        # assign value to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity
        # actions to execute
        Item.all_items.append(self)

    # set attribute
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self , value):
        if type(value) != str :
            raise Exception("name should only be an string")
        else:
            self.__name = value

    @property
    def price(self):
        return self.__name


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
        # this counts out the zeros
        if isinstance(num , float):
            return num.is_integer()
        elif isinstance(num , int):
            return True
        else :
            return False

    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
    def apply_increment(self , increment):
        self.__price  = self.__price + self.__price * increment

    def __repr__(self) :
        return  f"{self.__class__.__name__}( '{self.name}' , '{self.price}' , '{self.quantity}' )"





