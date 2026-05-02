

# Month keys
def getMonthKeys():
    month_keys = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    month_keys = [m.lower() for m in month_keys]
    return month_keys

# Name keys
def getNameKeys():
    name_keys = ["Nicholas", "Yang"]
    name_keys = [n.lower() for n in name_keys]
    return name_keys


# -------------------------------------------
# ----------- Expense type keys ------------
# -------------------------------------------

# Grocery keys
def getGroceryKeys():
    grocery_keys = ["wegmans", "target", "marketdistrict", "giant-eagle", "wal-mart","shop'n"]
    grocery_keys = [g.lower() for g in grocery_keys]
    return grocery_keys


# Household keys
def getHouseholdKeys():
    household_keys = ["iq", "verizon", "emeryflats"]
    household_keys = [h.lower() for h in household_keys]
    return household_keys

# Vehicle keys
def getVehicleKeys():
    vehicle_keys = ["sheetz","kellywoburn","honda","nissan","getgo","mobil","sunoco","shell"]
    vehicle_keys = [v.lower() for v in vehicle_keys]
    return vehicle_keys

# Travel keys
def getTravelKeys():
    travel_keys = ["courtyard","lyft","uber","delta","newslink","shadygrove","loganexpr"]
    travel_keys = [t.lower() for t in travel_keys]
    return travel_keys

# Healthcare keys 
def getHealthcareKeys():
    healthcare_keys = ["upmc","readingeyeassociates","walgreens"]
    healthcare_keys = [h.lower() for h in healthcare_keys]
    return healthcare_keys

# Clothes keys  
def getClothesKeys():
    clothes_keys = ["coach"]
    clothes_keys = [c.lower() for c in clothes_keys]
    return clothes_keys

# Subscription keys
def getSubscriptionKeys():
    subscription_keys = ["openai"]
    subscription_keys = [s.lower() for s in subscription_keys]
    return subscription_keys

# Gym keys
def getGymKeys():
    gym_keys = ["ymca"]
    gym_keys = [g.lower() for g in gym_keys]
    return gym_keys


# Dictionary of all categories
def getCategories():
    categories =  {
                    "grocery": getGroceryKeys(),
                    "household": getHouseholdKeys(),
                    "vehicle": getVehicleKeys(),
                    "travel": getTravelKeys(),
                    "healthcare": getHealthcareKeys(),
                    "clothes": getClothesKeys(),
                    "subscription": getSubscriptionKeys(),
                    "gym": getGymKeys(),
                    }
    return categories



if __name__ == "__main__":
    print("running inside key_setup.py")

    print(f"month keys:\n{month_keys}\n")
    print(f"name keys:\n{name_keys}\n")
    print(f"vehicle keys:\n{vehicle_keys}\n")
    print(f"travel keys:\n{travel_keys}\n")
    print(f"healthcare keys:\n{healthcare_keys}\n")
    print(f"clothes keys:\n{clothes_keys}\n")
    print(f"subscription keys:\n{subscription_keys}\n")
    print(f"gym keys:\n{gym_keys}\n")





