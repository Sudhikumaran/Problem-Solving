class Mobile:
    def __init__(self, brand,model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def display(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}"
    

mobile1 = Mobile("Iphone", "13 Pro", 74_000)
mobile2 = Mobile("Samsung", "m40" , 20_500)

print(mobile1.display())
print(mobile2.display())