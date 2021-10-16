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

def find_pet_by_name(pet, name):
    list_of_pets = pet["pets"]
    pet_list = {}

    
    for pets in list_of_pets:
       if pets["name"] == name:
         pet_list = pets
         return pet_list
        

def remove_pet_by_name(pet_shop, name):
    # list_of_pets = pet_shop["pets"]

    for animals in pet_shop["pets"]:
        # print(animals)
        
        if animals["name"] == name:
          pet_shop["pets"].remove(animals)


def add_pet_to_stock(pet_shop, name):
    pet_shop["pets"].append(name)

def get_customer_cash(cust):
    return cust["cash"]

def remove_customer_cash(cust,cash): 
    cust["cash"] = cust["cash"] - cash

def  get_customer_pet_count(pet_count):
    counter = 0
    for pet in pet_count["pets"]:
        counter += 1

    return counter    

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)



