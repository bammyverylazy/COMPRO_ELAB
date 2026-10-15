# ยังไม่ fix spacing

class CupOfCoffee:
    def __init__(self, coffee_type, drinking_type,price=0):
        self.coffee_type = coffee_type
        self.drinking_type = drinking_type
        self.add_on = []
        self.price = price
    def set_add_on(self, one_add_on, one_add_on_price):
        if one_add_on not in self.add_on:
            self.add_on.append(one_add_on)
            self.price += one_add_on_price
    def __repr__(self):
        if len(self.add_on) == 0:
            text = "no add on"
        elif len(self.add_on) ==1:
            text = f"{self.add_on[0]}"
        else:
            text = f'{", ".join(self.add_on[:-1])} and {self.add_on[-1]}'
        return f" This cup is {self.drinking_type.lower()} {self.coffee_type} with {text}, {self.price} baht."
    
class CustomerBill:
    def __init__(self, name):
        self.name = name
        self.ordered_coffee = []
    def add_ordered_coffee(self, aCupOfCoffeeObject):
        self.ordered_coffee.append(aCupOfCoffeeObject)

    def receipt(self):
        lines = [
            "++++++++++++++++++++++++++++++++",
            "     CPE38 **StarBUG Cafe",
            f"      Kun {self.name}'s Receipt",
            "++++++++++++++++++++++++++++++++",
            f"{'Description':<25}{'Price':>7}"
        ]

        total = 0

        for cup in self.ordered_coffee:
            description = f"{cup.drinking_type} {cup.coffee_type}"
            lines.append(f"{description:<25}{cup.price:>7}")

            for addon in cup.add_on:
                lines.append(f" + {addon}")

            total += cup.price

        lines.extend([
            " ",
            f"{'Total':<25}{total:>7}",
            "++++++++++++++++++++++++++++++++",
            " Thank you, please come back :)",
            "++++++++++++++++++++++++++++++++"
        ])

        return "\n".join(lines)

    

def readMenu(filename):
    menu = {}
    with open(filename) as f:
        for line in f:
            data = [x.strip() for x in line.strip().split(",")]
            if len(data) >= 4:
                menu[data[0]] = [
                    int(data[1]), int(data[2]), int(data[3])
                ]
            elif len(data) >= 2:
                menu[data[0]] = int(data[1])
    return menu

def show_menu():
    print("Welcome to CPE38 **StarBUG Cafe!")  
    print("+++++++++++++ MENU +++++++++++++")
    print("Coffee         Hot  Cold  Frappe")
    for i, (coffee, prices) in enumerate(coffee_menu_CSV.items(), 1):
        print(
            f"{i}.{coffee:<13}"
            f"{prices[0]:>5}{prices[1]:>6}{prices[2]:>7}"
        )

    print("++++++++++++ ADD-ON ++++++++++++")
    for i, (addon, price) in enumerate(add_on_menu_CSV.items(), 1):
        print(f"{i}.{addon:<20}{price:>5}")
    print("++++++++++++++++++++++++++++++++")
    print()
        
        
        
        

def runStarBUGcafe_main():
    coffees = list(coffee_menu_CSV.keys())
    addons = list(add_on_menu_CSV.keys())
    drinking_types = ["Hot", "Cold", "Frappe"]
    type_letters = ["H", "C", "F"]
    daily_sales = {}
    total_sold_amount = 0
    show_menu()
    while True:
        name = input("Enter customer's name: ")
        if name == "Good Day":
            break
        bill = CustomerBill(name)
        while True:
            try:
                cups = int(input("How many cups of coffee to order? "))
                if cups > 0:
                    break
            except ValueError:
                pass

            print(" ERROR: Invalid input!")
        for i in range(cups):
            # 1. Select coffee
            while True:
                try:
                    choice = int(input(
                        f"Cup #{i+1}, please select type of coffee: "
                    ))

                    if 1 <= choice <= len(coffees):
                        coffee_name = coffees[choice - 1]
                        break
                except ValueError:
                    pass
                print(" ERROR: Invalid input!")
            prices = coffee_menu_CSV[coffee_name]
            # 2. Find available drinking types
            available = [
                j for j, price in enumerate(prices)
                if price > 0
            ]
            if len(available) == 1:
                type_index = available[0]
            else:
                options = ",".join(
                    type_letters[j] for j in available
                )
                while True:
                    choice = input(
                        f"Cup #{i+1}, please select drinking type "
                        f"({options}): "
                    ).strip().upper()
                    if choice in type_letters:
                        type_index = type_letters.index(choice)
                        if type_index in available:
                            break
                    print(" ERROR: Invalid input!")
            drinking_name = drinking_types[type_index]
            base_price = prices[type_index]
            # 3. Create the coffee object
            cup = CupOfCoffee(
                coffee_name,
                drinking_name,
                base_price
            )
            # 4. Select add-ons
            while True:
                choice = input(
                    f"Cup #{i+1}, please select add on "
                    "(enter for exit): "
                ).strip()
                if choice == "":
                    break
                try:
                    addon_index = int(choice)

                    if not 1 <= addon_index <= len(addons):
                        print(" ERROR: Invalid input!")
                        continue
                except ValueError:
                    print(" ERROR: Invalid input!")
                    continue
                addon_name = addons[addon_index - 1]
                addon_price = add_on_menu_CSV[addon_name]
                if addon_price <= 0 or addon_name in cup.add_on:
                    print(" ERROR: Invalid input!")
                    continue
                cup.set_add_on(addon_name, addon_price)
            # 5. Save the coffee and update sales
            print(cup)
            bill.add_ordered_coffee(cup)
            daily_sales[coffee_name] = (
                daily_sales.get(coffee_name, 0) + 1
            )
            total_sold_amount += cup.price
        print(bill.receipt())
        show_menu()

    # Daily report
    print("++++++++++++++++++++++++++++++++")
    print("     CPE38 **StarBUG Cafe")
    print("  Report for Coffee sold today")
    print("++++++++++++++++++++++++++++++++")

    for coffee in coffees:
        count = daily_sales.get(coffee, 0)
        if count > 0:
            unit = "cup" if count == 1 else "cups"
            print(f"{coffee:<24}{count} {unit}")
    print()
    print(f"{'Total sold amount':<24}{total_sold_amount:>7} baht")
    print("++++++++++++++++++++++++++++++++")
    print("      What's a good day!")
    print("++++++++++++++++++++++++++++++++")

            
            
            
coffee_menu_filename = input('Enter Coffee Menu available today (filename): ')
coffee_menu_CSV = readMenu(coffee_menu_filename)
addon_menu_filename = input('Enter AddOn Menu available today (filename): ')
add_on_menu_CSV = readMenu(addon_menu_filename)

runStarBUGcafe_main()