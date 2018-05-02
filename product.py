class product:
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"
    def sell(self):
        self.status = "Sold"
        return self
    def add_tax(self, tax):
        self.total_price = (tax * self.price) + self.price
        return self.total_price 
    def returned_item(self, reason_for_return):
        if reason_for_return == "defective":
            self.price = 0
        elif reason_for_return =
            self.status = "For sale"
        elif reason_for_return == "used":
            self.status = "Used"
            self.price = self.price - (self.price * .20)
        return self
    def display_info(self):
        print(f"Price: {self.price} \nItem Name: {self.item_name} \nWeight: {self.weight} \nBrand: {self.brand} \nStatus: {self.status}")
        