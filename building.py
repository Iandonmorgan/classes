import datetime

class Building:
    def __init__(self, name, address, stories):
        self.designer = "Landon Morgan"
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories
        self.name = name
    
    def __str__(self):
        n1 = '\n'
        output = (
            f'{self.name}{n1}'
            f'{self.address}{n1}'
            f'Purchased by {self.owner} on {self.date_constructed} and has {self.stories} stories.{n1}'
            f'---------------------------------------------------'
        )
        return output
    
    def construct(self):
        self.date_constructed = datetime.datetime.now().strftime('%m-%d-%Y')

    def purchase(self, owner):
        self.owner = owner


# Create 5 building instances
# The_Cosmopolitan_Of_Las_Vegas = Building("The Cosmopolitan Of Las Vegas", "3708 S Las Vegas Blvd, Las Vegas, NV 89109", 61)
# Emirates_Palace = Building("Emirates Palace", "Corniche Rd W - Abu Dhabi - United Arab Emirates", 6)
# Resorts_World_Sentosa = Building("Resorts World Sentosa", "8 Sentosa Gateway, Singapore 098269", 12)
# Marina_Bay_Sands = Building("Marina Bay Sands", "10 Bayfront Avenue Hotel Towers, 1 2, 3, Singapore 018956", 57)
# Abraj_Al_Bait = Building("Abraj Al Bait", "AL HAJLAH MAKKAH CR ABRAJ AL-BAIT MALL, Mecca Saudi Arabia", 120)

# Have each one get purchased by a real estate magnate
# The_Cosmopolitan_Of_Las_Vegas.purchase("The Blackstone Group")
# Emirates_Palace.purchase("The Government of Abu Dhabi")
# Resorts_World_Sentosa.purchase("Genting Group")
# Marina_Bay_Sands.purchase("Las Vegas Sands")
# Abraj_Al_Bait.purchase("Saudi Overlords")

# After purchased, construct each one
# The_Cosmopolitan_Of_Las_Vegas.construct()
# Emirates_Palace.construct()
# Resorts_World_Sentosa.construct()
# Marina_Bay_Sands.construct()
# Abraj_Al_Bait.construct()

# Once all building are purchased and constructed, 
# print the address, owner, stories, and date constructed 
# to the terminal for each one.

#line 3 creates buildings list, line 13 adds class object into the buildings list

# for building in buildings:
    # print(building.name)
    # print(building.address)
    # print(f'Purchased by {building.owner} on {building.date_constructed} and has {building.stories} stories.')
    # print(f'---------------------------------------------------')