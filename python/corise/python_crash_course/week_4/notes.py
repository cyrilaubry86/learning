class Product:
    sales_tax = 0.07
    
    def __init__(self, name, price, nutrition_info):
        self.name = name
        self.price = price
        self.nutrition_info = nutrition_info

    @classmethod
    def make_free_bars(cls, name, nutrition_info):
        return cls(name, 0.00, nutrition_info)