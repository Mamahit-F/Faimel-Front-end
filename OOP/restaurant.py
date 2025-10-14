class Restaurant:
    def __init__(self):
        self.menu = {
            "Nasi Goreng": 15000,
            "Mie Goreng": 12000,
            "Nasi Padang": 25000,
            "Ayam Goreng": 18000,
            "Soto Ayam": 20000
        }
        self.order_list = []

    def show_menu(self):
        print("Menu")
        for item in self.menu:
            print("Rp.", self.menu[item], item)

    def order(self, item, qty):
        if item in self.menu:
            price = self.menu[item] * qty
            self.order_list.append((item, qty, price))
            print(qty, item, "added to order.")
        else:
            print(item, "not found in menu.")

    def buy(self):
        if len(self.order_list) > 0:
            print("Order Summary:")
            for order in self.order_list:
                print(order[1], order[0], "Rp.", order[2])
            total_price = sum(order[2] for order in self.order_list)
            print("Total Price Rp.", total_price)
        else:
            print("No order placed.")

class McDonaldRestaurant(Restaurant):
    def __init__(self):
        super().__init__()
        self.menu.update({
            "Burger": 20000,
            "Hotdog": 15908,
            "Fried Chicken": 25000,
            "French Fries": 10000,
            "Pizza": 30000
        })

restaurant = McDonaldRestaurant()

while True:
    print("Welcome to My Restaurant")
    print("1. Show Menu")
    print("2. Order")
    print("3. Buy")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        restaurant.show_menu()
    elif choice == 2:
        selected_item = input("Enter item name: ")
        num_item = int(input("Enter quantity: "))
        restaurant.order(selected_item, num_item)
    elif choice == 3:
        restaurant.buy()
    elif choice == 4:
        break
    else:
        print("Sorry, the number is not in the menu.")