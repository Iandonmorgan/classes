import datetime

class City:
    def __init__(self, name):
        self.mayor = "Landon Morgan"
        self.name = name
        self.year = datetime.datetime.now().strftime('%Y')
        self.buildings_list = []
    
    def add_building(self, building):
        self.buildings_list.append(building)