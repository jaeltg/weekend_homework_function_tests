# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]
   
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

#Can I include the previous function within this function?
def increase_pets_sold(pet_shop, pets):
    pet_shop["admin"]["pets_sold"] += pets

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    pets_filtered = []

    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pets_filtered.append(pet)

    return pets_filtered        

def find_pet_by_name(pet_shop, name):
    result_pet = None

    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            result_pet = pet

    return result_pet        

def remove_pet_by_name(pet_shop, name):

    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    new_pet = {
        "name": input("pets name: "), 
        "pet_type": input("pet type: "), 
        "breed": input("pet breed: "), 
        "price": input("pet price: ")
        }
    
    pet_shop["pets"].append(new_pet)
  
def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash

def get_customer_pet_count(customer):
    return len(customer["pets"])

# Adding a new pet or adding a pet from the stock to a customer?
def add_pet_to_customer(customer, new_pet):
    new_pet = {
        "name": input("pets name: "), 
        "pet_type": input("pet type: "), 
        "breed": input("pet breed: "), 
        "price": input("pet price: ")
        }

    customer["pets"].append(new_pet)    


            