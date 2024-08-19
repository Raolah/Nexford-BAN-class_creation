# Nexford-BAN-class_creation

## README

## POLICY MANAGEMENT SYSTEM FOR AN INSURANCE COMPANY

This is a project on creating a policy management system to manage policyholders, products, and payments of an insurance company in python. This system will allow policy managers to perform various tasks, such as adding and suspending policyholders, registering new members, and managing policy products. 


## INSTRUCTIONS

1.	Create distinct classes for policyholders, products, and payments, each in separate files.
2.	Implement methods within each class to fulfill the specified tasks.
3.	Demonstrate the functionality by creating at least two policyholders who have paid for one of the products. Display their account details.
4.	Submit your work as a zipped file or a link to your GitHub repository, including a README file with comprehensive instructions on accessing and utilizing your code

## Codes

The use of python in Vstudio
Creation on class in python

Policy Holder
```bash
class PolicyHolder
```
    
Product
```bash
class ProductMangemnet
```

Payment
```bash
class PaymentManagement
```    

## Defining Functions in the class

To run Pyton code use

PolicyHolder
```bash
def __init__(self, policyholder_id, name, contact_info, status='active'):
```

Product
```bash
def __init__(self, product_id, name, description, price, status='active'):
```

Payment
```bash
def __init__(self, payment_id, name, policyholder_id, payment_method, amount, due_date):
```

To make object instance by importing classes

```bash
from policyholder import PolicyHolder
from product import ProductMangement
from payment import PaymentManagement
from datetime import datetime
```

## PROCESS AND LESSONS LEARNED

Firstly, create a class for Policyholder and define functions and implement methods to register, suspend, and reactivate policyholders.

Methods:
```bash
def register_product(self, policy):
```

```bash
def suspend(self):
```

```bash
def reactivate(self):
```

Secondly, create a class for Product, define functions and implement methods for creating, updating, and removing/suspending policy products.

Methods:
```bash
def create(self, product):
```

```bash
def update(self):
```

```bash
def suspend(self):
```

```bash
def remove(self):
        self.status = 'remove'
```


Thirdly, create a class for Payment, define functions and implement methods for payment processing, reminders, and penalties.

Methods:
```bash
def payment_processing(self, payment_date):
```

```bash
def reminder(self):
```

```bash
def penalties(self, current_date):
```


Lastly, to display the account of two policyholder who have paid, we will create objects to display the account details by importing all .py files. The code to call the import files below:


main.py:
```bash
from policyholder import PolicyHolder
from product import ProductMangement
from payment import PaymentManagement
from datetime import datetime
```


Finally, when the  code is run the full account details of the two policyholders will be displayed.

NB: The python code was excuted in Vstudio.
