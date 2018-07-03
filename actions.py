# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.zain.com"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for store in stores:
        print(store.name)

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!

    #if store_name.lower() is in stores

    if store_name.lower() != "exit":
        for store in stores:
            if store.name.lower() == store_name.lower():
                print("Store found")
                print(store.name)
                return store
        print("Store not found")
        store_name = input("Please retype a store")
        get_store(store_name)
    else: 
        return



def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    user_input = input("Which store would you like to shop in?")
    picked_store = get_store(user_input)
    return picked_store

def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to cart.
    """
    # your code goes here!
    picked_store.print_products()
    user_picked_product = input("What would you like to buy? Type 'checkout' to checkout \n")
    while user_picked_product != "checkout":
        product_found = False
        for product in picked_store.products:
            if user_picked_product.lower() == product.name.lower():
                print("Product found")
                cart.add_to_cart(product)
                product_found = True
        if product_found:
            user_picked_product = input("What else? Type 'checkout' to checkout \n")
        else:
            print("Product not found.")
            user_picked_product = input("Please pick a valid product Type 'checkout' to checkout \n")




def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!
    print_stores()
    picked_store = pick_store()
    pick_products(cart, picked_store)
    cart.checkout()



    
    

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
