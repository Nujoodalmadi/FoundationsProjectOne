####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "bird"
signature_flavors = ["award winning carrot", "chocolate peanutbutter", "coconut candy bar", "decadent chocolate", "bird blue vanilla"]
order_list = []


def print_menu():

    for i in menu:
        print( i +  str(menu[i]) )
 


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    for i in original_flavors:
        print(i.capitalize())



def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    for i in signature_flavors:
        print(i.capitalize())



def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    if order in menu or order in original_flavors or order in signature_flavors:
        return True 
    else: 
        return False


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    order_input = input("Please enter your order. Type the word Exit once your done:")
    
    while order_input.lower() != "exit":
        
        if is_valid_order(order_input) == True:
            order_list.append(order_input)
        else:
            print("invalid")
            
        order_input= input("Please enter your order. Type the word Exit once your done:")
        
    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    if total > 5:
        return True
    else:
        return False


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    for i in order_list:
        if i in menu:
            total = total + menu[i]
        elif i in original_flavors:
            total = total + original_price
        else:
            total = total + signature_price
        
    return total
    
def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    for i in order_list:
        print(i)
    total = get_total_price(order_list)
    print("the total is: " + str(total) )
    if accept_credit_card(total):
          print("feel free to py by: cash or credit card")
    else:
          print("please pay by cash")
          
    print("Enjoy, Bird.")


