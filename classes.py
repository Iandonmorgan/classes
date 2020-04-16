class Pizza:
    def __init__(self):
        self.size = ""
        self.cheese = ""
        self.crust_type = ""
        self.toppings = []
    
    def add_topping(self, topping):
        self.toppings.append(topping)
    
    def print_order(self):
        sentence = f'I would like a {self.size}-inch, {self.crust_type} pizza, {self.cheese} cheese, with '
        if len(self.toppings) > 1:
            for topping in self.toppings:
                if topping != self.toppings[-1]:
                    sentence += f'{topping}, '
            else:
                sentence += f'and {self.toppings[-1]}.'
        elif len(self.toppings) == 1:
            sentence += f'{self.toppings[0]}.'
        else:
            sentence += f'no toppings.'
        print(sentence)