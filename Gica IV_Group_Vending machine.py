class VendingMachine:
    def __init__(self):
        self.products = {
            'A1': {'name': 'Chips', 'price': 30},
            'A2': {'name': 'Chocolate Bar', 'price': 25},
            'A3': {'name': 'Zest O', 'price': 15},
            'A4': {'name': 'Cookies', 'price': 40},
            'A5': {'name': 'Nuts', 'price': 35},
            'A6': {'name': 'Crackers', 'price': 20},
            'A7': {'name': 'Coca-Cola', 'price': 20},
            'A8': {'name': 'Pretzels', 'price': 25},
            'A9': {'name': 'Dried Fruits', 'price': 45},
        }

    def display_menu(self):
        print("Welcome to the Snack Vending Machine!")
        print("Available Products:")
        print("Code  |  Snack Name       |  Price")
        print("---------------------------------")
        for code, details in self.products.items():
            print(f"{code}  |  {details['name']:<16} |  P{details['price']:.2f}")

    def input_money(self):
        return float(input("Enter the amount of money (in PHP): "))

    def purchase(self, code, quantity, money):
        if code in self.products:
            snack = self.products[code]
            total_price = snack['price'] * quantity

            if money >= total_price:
                change = money - total_price
                print(f"You have purchased {quantity} {snack['name']}(s) for P{total_price:.2f}. Enjoy!")
                print(f"Your change: P{change:.2f}")
            else:
                print("Insufficient funds. Please add more money.")
        else:
            print("Invalid product code. Please select a valid product.")

if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.display_menu()

    product_code = input("Enter the product code (e.g., A1): ").upper()
    quantity = int(input("Enter the quantity: "))
    money = vending_machine.input_money()

    vending_machine.purchase(product_code, quantity, money)
