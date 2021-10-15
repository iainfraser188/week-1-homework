# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name (name):


    return name["name"]

def get_total_cash(cash):
    return cash["admin"]["total_cash"]

def add_or_remove_cash(num1,num2):
    num1["admin"]["total_cash"] = num2 + num1["admin"]["total_cash"]
    
def get_pets_sold(sold):
    return sold["admin"]["pets_sold"]





