def write_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data + '\n')

def read_from_file(filename): 
    with open(filename, 'r') as file:
        return file.readlines()


class Validation:
    @staticmethod
    def validate_phone(phone):
        if len(phone) == 9 and phone.startswith(('77', '78', '70', '73', '71')):
            return phone
        raise ValueError("Invalid phone number. Must be 9 digits and start with 77, 78, 70, 73, or 71.")


class Customer:

    def __init__(self, customer_id, name, phone, address):
        self.customer_id = customer_id
        self.name = name
        self.phone = Validation.validate_phone(phone)
        self.address = address
        write_to_file('customers.txt', f"{self.customer_id},{self.name},{self.phone},{self.address}")

class Game:
    def __init__(self, game_id, title, genre, price):
        self.game_id = game_id
        self.title = title
        self.genre = genre
        self.price = price
        
        write_to_file('games.txt', f"{self.game_id},{self.title},{self.genre},{self.price}")

class Console:
    def __init__(self, console_id, name, price):
        self.console_id = console_id
        self.name = name
        self.price = price
        write_to_file('consoles.txt', f"{self.console_id},{self.name},{self.price}")


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item.title if isinstance(item, Game) else item.name} to the cart.")

    def calculate_total(self):
        return sum([item.price for item in self.items])
   
    def show_cart(self):
        for item in self.items:
            print(f"{item.title if isinstance(item, Game) else item.name}: {item.price}")

class Discount:
    def __init__(self, discount_code, percentage):
        self.discount_code = discount_code
        self.percentage = percentage

    def apply_discount(self, total_price):
        return total_price - (total_price * (self.percentage / 100))


class Order:
    def __init__(self, order_id, customer, cart, total_price):
        self.order_id = order_id
        self.customer = customer
        self.cart = cart
        self.total_price = total_price
        write_to_file('orders.txt', f"{self.order_id},{self.customer.customer_id},{self.total_price}")
   
    def confirm_order(self):
        print(f"Order {self.order_id} confirmed for {self.customer.name}. Total: {self.total_price}")

class OrderHistory:
    def __init__(self):
        self.history = []

    def add_order(self, order):
        self.history.append(order)
        write_to_file('order_history.txt', f"Order ID: {order.order_id}, Customer: {order.customer.name}, Total: {order.total_price}")
   
    def view_order_history(self):
        for order in self.history:
            print(f"Order {order.order_id} for {order.customer.name}, Total: {order.total_price}")


class Inventory:
    def __init__(self):
        self.games = {}
        self.consoles = {}

    def add_game(self, game):
        if game.game_id not in self.games:
            self.games[game.game_id] = game
            print(f"Game '{game.title}' added to inventory.")
        else:
            print(f"Game '{game.title}' is already in the inventory.")

    def add_console(self, console):
        if console.console_id not in self.consoles:
            self.consoles[console.console_id] = console
            print(f"Console '{console.name}' added to inventory.")
        else:
            print(f"Console '{console.name}' is already in the inventory.")

    def check_stock(self, item_id, item_type):
        if item_type == 'game':
            return self.games[item_id].stock if item_id in self.games else 0
        elif item_type == 'console':
            return self.consoles[item_id].stock if item_id in self.consoles else 0


class Payment:
    def __init__(self, order, payment_method):
        self.order = order
        self.payment_method = payment_method
   
    def process_payment(self):
        print(f"Payment of {self.order.total_price} made using {self.payment_method}.")

class Store:
    def __init__(self):
        self.inventory = Inventory()
        self.customers = {}
        self.order_history = OrderHistory()

    def add_customer(self, customer):
        if customer.customer_id not in self.customers:
            self.customers[customer.customer_id] = customer
            print(f"Customer {customer.name} added to the store.")
        else:
            print(f"Customer {customer.name} already exists.")

    def create_order(self, customer_id, cart):
        if customer_id in self.customers:
            customer = self.customers[customer_id]
            total_price = cart.calculate_total()
            new_order = Order(len(self.order_history.history) + 1, customer, cart, total_price)
            new_order.confirm_order()
            self.order_history.add_order(new_order)
            return new_order
        else:
            print(f"Customer with ID {customer_id} not found.")
            return None

def get_input(prompt, validator=None):
    while True:
        try:
            value = input(prompt)
            if validator:
                return validator(value)
            return value
        except ValueError as e:
            print(f"Error: {e}")      
def main():
    store = Store()
    print("Welcome to the Gaming Store!")
    user_type = input("Are you an Employee or a Customer? (E/C): ").strip().lower()

    if user_type == 'e':
        print("Employee Access: Adding Games and Consoles to Inventory")
        while True:
            option = input("Do you want to add a (1) Game or (2) Console? (3 to exit): ")
            if option == '1':
                game_id = int(input("Enter Game ID: "))
                title = input("Enter Game Title: ")
                genre = input("Enter Game Genre: ")
                price = float(input("Enter Game Price: "))
                game = Game(game_id, title, genre, price)
                store.inventory.add_game(game)
            elif option == '2':
                console_id = int(input("Enter Console ID: "))
                name = input("Enter Console Name: ")
                price = float(input("Enter Console Price: "))
                
                console = Console(console_id, name, price)
                store.inventory.add_console(console)
            elif option == '3':
                break
            else:
                print("Invalid Option.")

    elif user_type == 'c':
        customer_id = input("Enter Customer ID: ")
        name = input("Enter Customer Name: ")
        phone = input("Enter Customer Phone: ")
        address = input("Enter Customer Address: ")
        customer = Customer(customer_id, name, phone, address)
        store.add_customer(customer)

        cart = Cart()

        # Show games and add to cart
        print("Available Games:")
        store.inventory.show_games()
        while True:
            game_id = int(input("Enter Game ID to add to cart (0 to stop): "))
            if game_id == 0:
                break
            if game_id in store.inventory.games:
                cart.add_item(store.inventory.games[game_id])
            else:
                print("Invalid Game ID.")

        # Show consoles and add to cart
        print("Available Consoles:")
        store.inventory.show_consoles()
        while True:
            console
main()