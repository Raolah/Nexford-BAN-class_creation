#Class creation for insurance company payment management 
from datetime import datetime

class PaymentManagement():
    def __init__(self, payment_id, policyholder_id, payment_method, amount, due_date):
        self.payment_id = payment_id
        self.policyholder_id = policyholder_id
        self.payment_method = payment_method
        self.amount = amount
        self.due_date = due_date
        self.status  = "unpaid"
        self.date = None
        self.payments = []

#Method impementation of payment process, reminder and panalities
    def payment_processing(self, payment_date):
        self.date = payment_date
        self.status = "paid"
        self.payments.append({
            'date': payment_date,
            'amount': self.amount,
            'status': self.status
        })
        
    def reminder(self):
        self.status = 'unpaid'
        print(f"Reminder: Payment {self.payment_id} for Policyholder {self.policyholder_id} with selected payment method {self.payment_method} amount {self.amount} is due on {self.due_date}.")


    def penalties(self, current_date):
        if self.status == "unpaid" and current_date > self.due_date:
            penalty = (current_date - self.due_date).days * 5  # A $5 penalty for late payment per day
            print(f"Payment {self.payment_id} is overdue. Penalty: ${penalty}.")
            return penalty
        return 0