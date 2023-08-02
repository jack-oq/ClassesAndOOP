#FoodClass.py

class Customer:
    def __init__(self, customerid, name, address, email, phone, member_status):
        self.customerid = customerid
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.member_status = member_status

    def customerid_attr(self):
        return self.customerid

    def name_attr(self):
        return self.name

    def address_attr(self):
        return self.address

    def email_attr(self):
        return self.email

    def phone_attr(self):
        return self.phone

    def is_member_attr(self):
        return self.member_status
    
class Transaction:
    def __init__(self, date,item_name, cost, customerid):
        self.date = date
        self.item_name = item_name
        self.cost = cost
        self.customerid = customerid

    def date_attr(self):
        return self.date

    def item_name_attr(self):
        return self.item_name

    def cost_attr(self):
        return self.cost

    def customerid_attr(self):
        return self.customerid
