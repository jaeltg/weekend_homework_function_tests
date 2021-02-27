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



            