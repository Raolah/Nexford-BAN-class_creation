#Class creation of insurance company product management 
class ProductMangement():
    def __init__(self, product_id, name, description, price, status='active'):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.status = status   #product management status starts as active
        self.products = []

#Method creation of product management
    def create(self, product):
        self.payments.append(product)

    def update(self):
        self.status = 'update'

    def suspend(self):
        self.status = 'suspend'
        
    def remove(self):
        self.status = 'remove'

    def display_product_details(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Price: ${self.price}")
        print(f"Status: {self.status}")
