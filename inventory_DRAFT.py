# Inventory class

import sqlite3
from tkinter import *
from tkinter import messagebox

conn = sqlite3.connect("inventory.db")

c = conn.cursor()


# c.execute("CREATE TABLE inventory(product text, quantity integer)")


class inventory:

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def getName(self):
        return self.name

    def getQuantity(self):
        return self.quantity

    def getInfo(self):
        print(self.name)
        print(str(self.quantity))

    def remove(self):
        volume = self.quantity
        volume = int(volume) - 1
        if volume <= 0:
            volume = 0
            self.quantity = volume
        self.quantity = str(volume)
        x = 0
        for items in items_in_store:
            Label(top, text="Product: " + items.getName() + " Quantity: " + str(items.getQuantity())).destroy()
            Button(top, text="+", command=items.add).destroy()
            x += 1

        x = 0
        for items in items_in_store:
            Label(top, text="Product: " + items.getName() + " Quantity: " + str(items.getQuantity())).grid(row=x,
                                                                                                           column=0)
            Button(top, text="+", command=items.add).grid(row=x, column=1)
            x += 1
            with conn:
                c.execute("UPDATE inventory SET quantity = :quantity WHERE product = :product",
                          {'product': items.getName(), 'quantity': items.getQuantity()})

    def add(self):
        global top
        volume = self.quantity
        volume = int(volume) + 1
        self.quantity = str(volume)
        x = 0
        for items in items_in_store:
            Label(top, text="Product: " + items.getName() + " Quantity: " + str(items.getQuantity())).destroy()
            Button(top, text="+", command=items.add).destroy()
            x += 1

        x = 0
        for items in items_in_store:
            Label(top, text="Product: " + items.getName() + " Quantity: " + str(items.getQuantity())).grid(row=x,
                                                                                                           column=0)
            Button(top, text="+", command=items.add).grid(row=x, column=1)
            x += 1
            with conn:
                c.execute("UPDATE inventory SET quantity = :quantity WHERE product = :product",
                          {'product': items.getName(), 'quantity': items.getQuantity()})

    def delete_product(self):
        global top
        with conn:
            c.execute("DELETE FROM inventory WHERE product = :product", {'product': self.name})
        if self in items_in_store:
            items_in_store.remove(self)
        top.destroy()
        global hip
        top = Toplevel()
        x = 0
        for items in items_in_store:
            Label(top, text="Product: " + items.getName() + " Quantity: " + str(items.getQuantity())).grid(row=x,
                                                                                                           column=0)
            Button(top, text="DELETE", command=items.delete_product).grid(row=x, column=1)
            x += 1


def new_item():
    global top
    global new
    global new_quantity
    new_item_name = new.get()
    new_item_quantity = new_quantity.get()
    response = messagebox.askquestion("Confirm",
                                      "Item name: " + new_item_name + "\nItem Quantity: " + new_item_quantity + "\nIs the information you added correct?")
    if response == "yes":
        item = inventory(new_item_name, new_item_quantity)
        items_in_store.append(item)
        with conn:
            c.execute("INSERT INTO inventory VALUES (:product, :quantity)",
                      {'product': item.getName(), 'quantity': item.getQuantity()})
        top.destroy()
    else:
        Label(top, text="Please correct the information").grid(row=4, column=0, columnspan=2)


def add_item():
    global top
    top = Toplevel()
    Label(top, text="Name of Item: ").grid(row=0, column=0)
    global new
    new = StringVar()
    Entry(top, textvariable=new).grid(row=0, column=1)
    global new_quantity
    new_quantity = StringVar()
    Label(top, text="Quantity of Item: ").grid(row=1, column=0)
    Entry(top, textvariable=new_quantity).grid(row=1, column=1)

    Button(top, text="Ok", command=new_item).grid(row=3, column=1, columnspan=2)


def modify_inventory():
    global top
    top = Toplevel()
    x = 0
    for items in items_in_store:
        Label(top, text="Product: " + items.getName() + " Quantity: " + str(items.getQuantity())).grid(row=x, column=0)
        Button(top, text="+", command=items.add).grid(row=x, column=1)
        Button(top, text="-", command=items.remove).grid(row=x, column=2)
        x += 1


def delete_page():
    global top
    top = Toplevel()
    x = 0
    for items in items_in_store:
        Label(top, text="Product: " + items.getName() + " Quantity: " + str(items.getQuantity())).grid(row=x, column=0)
        Button(top, text="DELETE", command=items.delete_product).grid(row=x, column=1)
        x += 1
    return


items_in_store = []
c.execute("SELECT * FROM inventory")
it = list(c.fetchall())
y = 0
for i in it:
    x = inventory(i[0], i[1])
    y += 1
    items_in_store.append(x)

root = Tk()
root.title("Inventory")
root.geometry("400x400")
if len(items_in_store) == 0:
    pop = messagebox.showinfo("Welcome!", "To begin please add items to your inventory list")
add_new_item = Button(root, text="Add New Item", command=add_item).pack(pady=50)
modify = Button(root, text="View All Inventory", command=modify_inventory).pack(pady=50)
delete = Button(root, text="Delete an Item", command=delete_page).pack(pady=50)

##category = Label(root, text = "Create a category").pack()
##frame = LabelFrame(root, text = "Categories", padx=5, pady=5)
##frame.pack()
##c1 = Button(frame, text = "button")
##c1.grid(row = 0, column = 0)

conn.commit()

root.mainloop()
