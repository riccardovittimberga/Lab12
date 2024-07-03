from dataclasses import dataclass
from datetime import datetime


@dataclass
class Product:
    Retailer_code:int
    Product_number:int
    Order_method_code:int
    Date:datetime
    Quantity:int
    Unit_price:float
    Unit_sale_price:float

    def __hash__(self):
        return hash(self.Retailer_code)

    def __eq__(self, other):
        return self.Retailer_code==other.Retailer_code

    def __str__(self):
        pass