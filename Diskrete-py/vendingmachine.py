import tkinter as tk
from tkinter import messagebox

class VendingMachine:
    def __init__(self):
        self.items = {
            "A1": ("KitKat", 30),
            "A2": ("Peanut Butter Cups", 28),
            "A3": ("Hershey's Bar", 39),
            "B1": ("Jolly Rancher", 38),
            "B2": ("M&Ms", 40),
            "B3": ("Cadbury", 52),
            "C1": ("Snickers", 45),
            "C2": ("Reese's Pieces", 47),
            "C3": ("Hershey's Nuggets", 56)
        }

    def vend(self, code, quantity, money):
        if code in self.items:
            item, price = self.items[code]
            total_price = price * quantity
            if money >= total_price:
                return (f"You selected {quantity} {item}(s), it costs P{total_price}.", money - total_price)
            else:
                return (f"You don't have enough money for {quantity} {item}(s). It costs P{total_price}.", money)
        else:
            return (f"Invalid selection: {code}", money)

def purchase():
    code = code_entry.get()
    quantity = int(quantity_entry.get())
    money = int(money_entry.get())
    message, change = vending_machine.vend(code, quantity, money)
    messagebox.showinfo("Purchase Result", message)
    change_label.config(text=f"Your change is: P{change}")

vending_machine = VendingMachine()

root = tk.Tk()
root.title("Vending Machine")

items_listbox = tk.Listbox(root, height=10, width=30)  # Adjust the width as needed
for code, (item, price) in vending_machine.items.items():
    items_listbox.insert(tk.END, f"{code}: {item} - P{price}")
items_listbox.pack()

code_label = tk.Label(root, text="Enter the code of the item you want to purchase:")
code_label.pack()

code_entry = tk.Entry(root)
code_entry.pack()

quantity_label = tk.Label(root, text="Enter the quantity:")
quantity_label.pack()

quantity_entry = tk.Entry(root)
quantity_entry.pack()

money_label = tk.Label(root, text="Enter the amount of money you have:")
money_label.pack()

money_entry = tk.Entry(root)
money_entry.pack()

purchase_button = tk.Button(root, text="Purchase", command=purchase)
purchase_button.pack()

change_label = tk.Label(root, text="")
change_label.pack()

root.mainloop()
