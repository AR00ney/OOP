#========The beginning of the class==========
# creat Shoe class init variables __str__ for format output
# define get_cost and get_quantity functions
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    def __str__(self):
        return f'{self.country},{self.code},{self.product},{self.cost},{self.quantity}'

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity