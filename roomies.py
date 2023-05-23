roomies = ["Liela", "Ben", "Alec", "Lando", "Vashti"]

# Utilities Are Due Once A Month and Are Varied in price
googleFiber=80

power = 131.34

water = 200

dominionGas = 22.46




for roomie in roomies:
    total_cost = 4000
    utilities = googleFiber + power + water 
    share_of_rent = total_cost / len(roomies)
    share_of_utilities = utilities / len(roomies)
    total_payment = share_of_rent + share_of_utilities
    print(f"{roomie} needs to pay ${total_payment} for rent and utilities.")