from city import City
from building import Building

Landopolis = City("Landopolis")

print(f'{Landopolis.mayor}, Mayor of {Landopolis.name}')
print(f'---------------------------------------------------')

The_Cosmopolitan_Of_Las_Vegas = Building("The Cosmopolitan Of Las Vegas", "3708 S Las Vegas Blvd, Las Vegas, NV 89109", 61)
Emirates_Palace = Building("Emirates Palace", "Corniche Rd W - Abu Dhabi - United Arab Emirates", 6)
Resorts_World_Sentosa = Building("Resorts World Sentosa", "8 Sentosa Gateway, Singapore 098269", 12)
Marina_Bay_Sands = Building("Marina Bay Sands", "10 Bayfront Avenue Hotel Towers, 1 2, 3, Singapore 018956", 57)
Abraj_Al_Bait = Building("Abraj Al Bait", "AL HAJLAH MAKKAH CR ABRAJ AL-BAIT MALL, Mecca Saudi Arabia", 120)

The_Cosmopolitan_Of_Las_Vegas.purchase("The Blackstone Group")
Emirates_Palace.purchase("The Government of Abu Dhabi")
Resorts_World_Sentosa.purchase("Genting Group")
Marina_Bay_Sands.purchase("Las Vegas Sands")
Abraj_Al_Bait.purchase("Saudi Overlords")

The_Cosmopolitan_Of_Las_Vegas.construct()
Emirates_Palace.construct()
Resorts_World_Sentosa.construct()
Marina_Bay_Sands.construct()
Abraj_Al_Bait.construct()

Landopolis.buildings_list.extend([The_Cosmopolitan_Of_Las_Vegas, Emirates_Palace, Resorts_World_Sentosa, Abraj_Al_Bait, Marina_Bay_Sands])

for building in Landopolis.buildings_list:
    print(building)