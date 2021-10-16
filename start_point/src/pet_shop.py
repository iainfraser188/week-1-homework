# WRITE YOUR FUNCTIONS HERE
# import pdb
def get_pet_shop_name (name):


    return name["name"]

def get_total_cash(cash):
    return cash["admin"]["total_cash"]

def add_or_remove_cash(num1,num2):
    num1["admin"]["total_cash"] = num2 + num1["admin"]["total_cash"]
    
def get_pets_sold(sold):
    return sold["admin"]["pets_sold"]

def increase_pets_sold(initial_sold,new_sold):
    initial_sold["admin"]["pets_sold"] = new_sold + initial_sold["admin"]["pets_sold"]

def get_stock_count(stock):
    stocklist = stock["pets"]

    counter = 0
    
    for animal in stocklist:

     counter += 1
    return counter

def get_pets_by_breed(pet, breed):
    animal_list = pet["pets"]
    pet_list = []

    for animals in animal_list:
        if animals["breed"] == breed:
          
          pet_list.append(animals)

    return pet_list 









