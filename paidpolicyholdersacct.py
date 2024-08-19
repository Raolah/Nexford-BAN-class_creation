# main.py

from policyholder import PolicyHolder
from product import ProductMangement
from payment import PaymentManagement
from datetime import datetime

#Objects creation for all the classes
#Create some products
product1 = ProductMangement(101, "Health Insurance", "Comprehensive health coverage", 200)
product2 = ProductMangement(102, "Car Insurance", "Term Car insurance", 150)

#Register policyholders
policyholder1 = PolicyHolder(1, "Mark Anthony", "23 Cresent Street")
policyholder2 = PolicyHolder(2, "Salam Hayek", "456 Allen Avenue")

#Policyholders purchase products
policyholder1.register_product(product1)
policyholder2.register_product(product2)

#Creating an instance for payment process
payment1 = PaymentManagement(1, policyholder1.policyholder_id, "Credit Card", 200, datetime(2024, 9, 1))
payment2 = PaymentManagement(2, policyholder2.policyholder_id, "Cash Paymnet", 150, datetime(2024, 9, 10))

#Call method on the payment1 and payment2 object
#Processing the payment
payment1.payment_processing(datetime(2024, 8, 31))
payment2.reminder()

# Display policyholder details
print("Policyholder 1 Details:")
policyholder1.get_policyholder_details()

print("\nPolicyholder 2 Details:")
policyholder2.get_policyholder_details()

# Calculate penalties (assuming today is 2024-09-15)
penalty = payment2.penalties(datetime(2024, 9, 15))
print(f"Penalty for Policyholder 2: ${penalty}")