from classes import Pizza

meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.cheese = "extra"
meat_lovers.crust_type = "Deep dish"
meat_lovers.add_topping("Pepperoni")
meat_lovers.add_topping("Olives")
meat_lovers.print_order()

veggie = Pizza()
veggie.size = 14
veggie.crust_type = "Regular"
veggie.cheese = "no"
veggie.add_topping("Banana Peppers")
veggie.add_topping("Olives")
veggie.add_topping("Mushrooms")
veggie.add_topping("Pineapple")
veggie.add_topping("Onions")
veggie.add_topping("Roasted Red Peppers")
veggie.print_order()