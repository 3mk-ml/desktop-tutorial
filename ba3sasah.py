import os

# classes:
# 1.Customer
# 2.Game
# 3.Console
# 4.employee
# 5.store
# 6.inventory
# 7.validation
# 8.laptop
# 9.controllers

def cls(): 
    os.system('cls' if os.name=='nt' else 'clear')

def write_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data + '\n')

def read_from_file(filename):
    with open(filename, 'r') as file:
        f_contents = file.read()
        print(f_contents)


class Validation:
    @staticmethod
    def validate_phone(phone):
        if len(phone) == 9 and phone.startswith(('77', '78', '70', '73', '71')):
            return phone
        raise ValueError("Invalid phone number. Must be 9 digits and start with 77, 78, 70, 73, or 71.")

class employee:
    def __init__(self, employee_id, name, phone, address):
        self.employee_id = employee_id
        self.name = name
        self.phone = Validation.validate_phone(phone)
        self.address = address
        write_to_file('employees.txt', f"employee ID: {self.employee_id}\nemployee name: {self.name}\nemployee phone number: {self.phone}\nemployee address: {self.address}\n")

def getEmployeeInfo():
    cls()
    employee_id = get_input("Enter employee ID: ")
    cls()
    name = get_input("Enter employee Name: ")
    cls()
    phone = get_input("Enter employee Phone: ", Validation.validate_phone)
    cls()
    address = get_input("Enter employee Address: ")
    cls()
    employeeToAdd = employee(employee_id, name, phone, address)
    
    myStore.add_employee(employeeToAdd)
    
    print("choose 1 for main menu")
    choice = int(input("choice: "))
    if choice == 1:
        start()
    else:
        pass

class Customer:
    def __init__(self, customer_id, name, phone, address):
        self.customer_id = customer_id
        self.name = name
        self.phone = Validation.validate_phone(phone)
        self.address = address
        write_to_file('customers.txt', f"Customer ID: {self.customer_id}\nCustomer name: {self.name}\nCustomer phone number: {self.phone}\nCustomer address: {self.address}\n")

def getCustomerInfo():
    cls()
    customer_id = get_input("Enter Customer ID: ")
    cls()
    name = get_input("Enter Customer Name: ")
    cls()
    phone = get_input("Enter Customer Phone: ", Validation.validate_phone)
    cls()
    address = get_input("Enter Customer Address: ")
    cls()
    customer = Customer(customer_id, name, phone, address)
    myStore.add_customer(customer)
    
    print("choose 1 for main menu")
    choice = int(input("choice: "))
    if choice == 1:
        start()
    else:
        pass

class Game:
    def __init__(self, game_id, title, genre, price):
        self.game_id = game_id
        self.title = title
        self.genre = genre
        self.price = price
        write_to_file('games.txt', f"Game ID: {self.game_id}\nGame name: {self.title}\nGame gener: {self.genre}\nGame price: {self.price}\n")

def addGame():
    id = input("game id: ")
    name = input("game name: ")
    gener = input("game gener: ")
    price = input("game price: ")
    toAdd = Game(id, name, gener, price)
    print(f"Game '{toAdd.title}' added to inventory.")
    print("choose 1 to add another game.\n")
    print("choose 2 for main menu.\n")
    choice = int(input("choice: "))
    if choice == 1:
        addGame()
    else:
        start()


class Console:
    def __init__(self, console_id, name, price):
        self.console_id = console_id
        self.name = name
        self.price = price
        write_to_file('consoles.txt', f"Console ID: {self.console_id}\nConsole name: {self.name}\nConsole price: {self.price}\n")

def addConsole():
    id = input("Console id: ")
    name = input("Console name: ")
    price = input("Console price: ")
    toAdd = Console(id, name, price)
    print(f"The '{toAdd.name}' is added to inventory.")
    print("choose 1 to add another console.\n")
    print("choose 2 for main menu.\n")
    choice = int(input("choice: "))
    if choice == 1:
        addConsole()
    else:
        start()

class Laptop:
    def __init__(self, laptop_id, name, gpu, cpu, price):
        self.laptop_id = laptop_id
        self.name = name
        self.price = price
        self.gpu = gpu
        self.cpu = cpu
        write_to_file('laptop.txt', f"laptop ID: {self.laptop_id}\nlaptop name: {self.name}\nlaptop GPU: {self.gpu}\nlaptop CPU: {self.cpu}\nlaptop price: {self.price}\n")


def addLaptop():
    id = input("laptop id: ")
    name = input("laptop name: ")
    gpu = input("laptop GPU: ")
    cpu = input("laptop CPU: ")
    price = input("laptop price: ")
    toAdd = Laptop(id, name, gpu, cpu, price)
    print(f"The '{toAdd.name}' is added to inventory.")
    print("choose 1 to add another laptop.\n")
    print("choose 2 for main menu.\n")
    choice = int(input("choice: "))
    if choice == 1:
        addLaptop()
    else:
        start()

class Controller:
    def __init__(self, controller_id, name, price):
        self.controller_id = controller_id
        self.name = name
        self.price = price
        write_to_file('controller.txt', f"controller ID: {self.controller_id}\ncontroller name: {self.name}\ncontroller price: {self.price}\n")


def addController():
    id = input("controller id: ")
    name = input("controller name: ")
    price = input("controller price: ")
    toAdd = Controller(id, name, price)
    print(f"The '{toAdd.name}' is added to inventory.")
    print("choose 1 to add another controller.\n")
    print("choose 2 for main menu.\n")
    choice = int(input("choice: "))
    if choice == 1:
        addController()
    else:
        start()


class Inventory:
    def __init__(self):
        self.games = {}
        self.consoles = {}
        self.laptop = {}
        self.controller = {}

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

    def add_laptop(self, laptop):
        if laptop.laptop_id not in self.laptop:
            self.laptop[laptop.laptop_id] = laptop
            print(f"Laptop '{laptop.name}' added to inventory.")
        else:
            print(f"Laptop '{laptop.name}' is already in the inventory.")

    def add_controller(self, controller):
        if controller.controller_id not in self.controller:
            self.controllers[controller.controller_id] = controller
            print(f"controller '{controller.controller_id}' added to inventory.")
        else:
            print(f"controller '{controller.controller_id}' is already in the inventory.")



class Store:
    def __init__(self):
        self.customers = {}
        self.employees = {}
        # self.order_history = OrderHistory()

    def add_employee(self, employee):
        if employee.employee_id not in self.employees:
            self.employees[employee.employee_id] = employee
            print(f"Employee {employee.name} added to the store.\n")
        else:
            print(f"Employee {employee.name} already exists.\n")

    def add_customer(self, customer):
        if customer.customer_id not in self.customers:
            self.customers[customer.customer_id] = customer
            print(f"Customer {customer.name} added to the store.\n")
        else:
            print(f"Customer {customer.name} already exists.\n")

    
def get_input(prompt, validator=None):
    while True:
        try:
            value = input(prompt)
            if validator:
                return validator(value)
            return value
        except ValueError as e:
            print(f"Error: {e}")

def toList():
    cls()
    print("press 1 to list games archives.\n")
    print("press 2 to list consoles archives.\n")
    print("press 3 to list laptops archives.\n")
    print("press 4 to list controllers archives.\n")
    print("press 5 to list employees archives.\n")
    print("press 6 to list customers archives.\n")
    print("press 7 for main menu\n")
    choice = int(input("Choice: "))
    cls()
    
    if choice == 1:
        read_from_file('games.txt')
    elif choice == 2:
        read_from_file('consoles.txt')
    elif choice == 3:
        read_from_file('laptop.txt')
    elif choice == 4:
        read_from_file('controller.txt')
    elif choice == 5:
        read_from_file('employees.txt')
    elif choice == 6:
        read_from_file('customers.txt')
        print()    
    else:
        start()

def start():
    cls()
    print("choose 1 to add a game.\n")
    print("choose 2 to add a console.\n")
    print("choose 3 to add a laptop.\n")
    print("choose 4 to add a controller.\n")
    print("choose 5 to add an employee.\n")
    print("choose 6 to add a customer.\n")
    print("choose 7 to list an archive.\n")
    choice = int(input("choice: "))
    if choice == 1:
        addGame()
    elif choice == 2:
        addConsole()
    elif choice == 3:
        addLaptop()
    elif choice == 4:
        addController()
    elif choice == 5:
        getEmployeeInfo()
    elif choice == 6:
        getCustomerInfo()
    elif choice == 7:
        toList()
    else:
        start()  

myStore = Store()
myInventory = Inventory()
# myCart = Cart()

start()