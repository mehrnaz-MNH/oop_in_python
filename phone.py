from item import Item

class Phone(Item):
    # every time an object is made , the constructor gets called
    def __init__(self , name:str, price:float , quantity = 0 , broken_phones = 0) : # constructor

        # call the super function to inheret all the attributes of parent class
        super().__init__(
            name , price , quantity
        )
        # run validation
        assert broken_phones >= 0,f"the {broken_phones} is not greater than 0 "
        # assign value to self object
        self.broken_phones = broken_phones
