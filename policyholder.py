#Class creation for policyholder
class PolicyHolder:
    def __init__(self, policyholder_id, name, contact_info, status='active'):
        self.policyholder_id = policyholder_id
        self.name = name
        self.contact_info = contact_info
        self.status = status   #Policyholder status starts as active
        self.product = []

#Method impementation of register products, suspend and reactivate
    def register_product(self, policy):
        
        if self.status == "active":
            self.product.append(policy)
    
        else:
            print(f"Cannot add product. Policyholder {self.name} is suspended.")

    def suspend(self):
        self.status = 'suspended'

    def reactivate(self):
        self.status = 'active'

    def get_policyholder_details(self):
        print(f"Policyholder ID: {self.policyholder_id}")
        print(f"Name: {self.name}")
        print(f"Contact Info: {self.contact_info}")
        print(f"Status: {self.status}")
        print("Products:")
        for product in self.product:
            print(f"  - {product.name} (${product.price})")


