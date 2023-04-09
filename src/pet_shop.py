def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop,amount_sold):
    pet_shop["admin"]["pets_sold"] += amount_sold 

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, pet_breed):
    breed_of_pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == pet_breed:
            breed_of_pets.append(pet)
    return breed_of_pets

def find_pet_by_name(pet_shop,pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name: 

         return pet 

def remove_pet_by_name(pet_shop, name):
   pet_to_remove = find_pet_by_name(pet_shop, name)
   pet_shop["pets"].remove(pet_to_remove) 
       
def add_pet_to_stock(pet_shop,new_pet):
    return pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer) :
    return len(customer["pets"])

def add_pet_to_customer(customer,new_pet):
    return customer["pets"].append(new_pet)

#OPTIONAL

def customer_can_afford_pet(customer,cash):
    cash = customer["cash"] 
    if cash >= 100:
        return True
    
    return False