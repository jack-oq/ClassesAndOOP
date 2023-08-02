from FoodClass import Customer
from FoodClass import Transaction

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]


dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
        'trans2':['2/15/2023','The Octobreakfast',18,569],
        'trans3':['2/15/2023','The Octoveg',16,570],
        'trans4':['2/15/2023','The Octoburger',20,570],
}

#The two different customer instances, comment/uncomment to switch between the two:

#customer = Customer(569, "Aubree Himsworth", "1172 Moulton Hill Waco Texas 76710", "ahimsworthfs@list-manage.com", "254-555-2273", True)
customer = Customer(570, "Danni Sellyar", "97 Mitchell Way Hewitt Texas 76712", "dsellyarft@gmpg.org", "254-555-9362", False)

ID = customer.customerid_attr()

trans1 = Transaction(dict['trans1'][0], dict['trans1'][1], dict['trans1'][2], dict['trans1'][3])
trans2 = Transaction(dict['trans2'][0], dict['trans2'][1], dict['trans2'][2], dict['trans2'][3])
trans3 = Transaction(dict['trans3'][0], dict['trans3'][1], dict['trans3'][2], dict['trans3'][3])
trans4 = Transaction(dict['trans4'][0], dict['trans4'][1], dict['trans4'][2], dict['trans4'][3])

def display_report(customer, ID):
        total_cost = 0

        print()
        print(f"Customer Name: {customer.name_attr()}")
        print(f"Phone Number: {customer.phone_attr()}")

        transactions_list = []
    
        #find which transactions match with ID and add those to list
        for key, value in dict.items():
                if value[3] == ID:
                        transactions_list.append(Transaction(value[0], value[1], value[2], value[3]))
        
        #display and add cost to running total
        for transaction in transactions_list:
                print(f"Order Item: {transaction.item_name_attr()} - Cost: ${transaction.cost_attr():.2f}")
                total_cost += transaction.cost_attr()

        #factor in member discount
        if customer.is_member_attr():
                discount = total_cost * 0.2
                discounted_price = total_cost - discount
                print(f"Member Discount: ${discount:.2f}")
                print(f"Total Cost after discount: ${discounted_price:.2f}")
        else:
                print(f"Total Cost: ${total_cost:.2f}")

        print()

display_report(customer, ID)
