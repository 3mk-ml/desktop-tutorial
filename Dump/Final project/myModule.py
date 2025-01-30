import os
from datetime import date
import time

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
        today = date.today()
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        write_to_file('employees.txt', f"Date: {today}\nTime: {current_time}\nemployee ID: {self.employee_id}\nemployee name: {self.name}\nemployee phone number: {self.phone}\nemployee address: {self.address}\n")

class Customer:
    def __init__(self, customer_id, name, phone, address):
        self.customer_id = customer_id
        self.name = name
        self.phone = Validation.validate_phone(phone)
        self.address = address
        today = date.today()
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        write_to_file('customers.txt', f"Date: {today}\nTime: {current_time}\nCustomer ID: {self.customer_id}\nCustomer name: {self.name}\nCustomer phone number: {self.phone}\nCustomer address: {self.address}\n")

class Game:
    def __init__(self, game_id, name, genre, price, quantity):
        self.game_id = game_id
        self.name = name
        self.genre = genre
        self.price = price
        self.quantity = quantity
        today = date.today()
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        write_to_file('games.txt', f"Date: {today}\nTime: {current_time}\nGame ID: {self.game_id}\nGame name: {self.name}\nGame gener: {self.genre}\nGame price: {self.price}\nQuantity: {self.quantity}\n")

class Console:
    def __init__(self, console_id, name, price, quantity):
        self.console_id = console_id
        self.name = name
        self.price = price
        self.quantity = quantity
        today = date.today()
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        write_to_file('consoles.txt', f"Date: {today}\nTime: {current_time}\nConsole ID: {self.console_id}\nConsole name: {self.name}\nConsole price: {self.price}\nQuantity: {self.quantity}\n")

class PC:
    def __init__(self, pc_id, name, gpu, cpu, motherBord, price, quantity):
        self.pc_id = pc_id
        self.name = name
        self.price = price
        self.gpu = gpu
        self.cpu = cpu
        self.motherBord = motherBord
        self.quantity = quantity
        today = date.today()
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        write_to_file('PCs.txt', f"Date: {today}\nTime: {current_time}\nPC's ID: {self.pc_id}\nPC's name: {self.name}\nPC's GPU: {self.gpu}\nPC's CPU: {self.cpu}\nPC's motherbord: {self.motherBord}\nPC's price: {self.price}\nQuantity: {self.quantity}\n")

class Laptop:
    def __init__(self, laptop_id, name, gpu, cpu, price, quantity):
        self.laptop_id = laptop_id
        self.name = name
        self.price = price
        self.gpu = gpu
        self.cpu = cpu
        self.quantity = quantity
        today = date.today()
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        write_to_file('laptopes.txt', f"Date: {today}\nTime: {current_time}\nlaptop ID: {self.laptop_id}\nlaptop name: {self.name}\nlaptop GPU: {self.gpu}\nlaptop CPU: {self.cpu}\nlaptop price: {self.price}\nQuantity: {self.quantity}\n")

class Controller:
    def __init__(self, controller_id, name, price, quantity):
        self.controller_id = controller_id
        self.name = name
        self.price = price
        self.quantity = quantity
        today = date.today()
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        write_to_file('controlleres.txt', f"Date: {today}\nTime: {current_time}\nController ID: {self.controller_id}\nController name: {self.name}\nController price: {self.price}\nQuantity: {self.quantity}\n")

class Mobile:
    def __init__(self, mobile_id, name, storage, price, quantity):
        self.mobile_id = mobile_id
        self.name = name
        self.storage = storage
        self.price = price
        self.quantity = quantity
        today = date.today()
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        write_to_file('mobiles.txt', f"Date: {today}\nTime: {current_time}\nMobile ID: {self.mobile_id}\nMobile name: {self.name}\nMobile storage: {self.storage}\nMobile price: {self.price}\nQuantity: {self.quantity}\n")

class Monitor:
    def __init__(self, monitor_id, name, size, price, quantity):
        self.monitor_id = monitor_id
        self.name = name
        self.size = size
        self.price = price
        self.quantity = quantity
        today = date.today()
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        write_to_file('monitors.txt', f"Date: {today}\nTime: {current_time}\nMonitor ID: {self.monitor_id}\nMonitor name: {self.name}\nMonitor size: {self.size}\nMonitor price: {self.price}\nQuantity: {self.quantity}\n")

class Inventory:
    def __init__(self):
        self.games = {}
        self.consoles = {}
        self.laptopes = {}
        self.controllers = {}
        self.mobiles = {}
        self.monitors = {}
        self.PC = {}

    def add_game(self, game):
        if game.game_id not in self.games:
            self.games[game.game_id] = game
            print(f"The Game {game.name} added to inventory.\n")
        else:
            print(f"The Game {game.name} is already in the inventory.\n")

    def add_console(self, console):
        if console.console_id not in self.consoles:
            self.consoles[console.console_id] = console
            print(f"The Console {console.name} added to inventory.\n")
        else:
            print(f"The Console {console.name} is already in the inventory.\n")

    def add_PC(self, PC):
        if PC.pc_id not in self.PC:
            self.PC[PC.pc_id] = PC
            print(f"The PC {PC.name} added to inventory.\n")
        else:
            print(f"The PC {PC.name} is already in the inventory.\n")


    def add_laptop(self, laptop):
        if laptop.laptop_id not in self.laptopes:
            self.laptopes[laptop.laptop_id] = laptop
            print(f"The Laptop {laptop.name} added to inventory.\n")
        else:
            print(f"The Laptop {laptop.name} is already in the inventory.\n")

    def add_controller(self, controller):
        if controller.controller_id not in self.controllers:
            self.controllers[controller.controller_id] = controller
            print(f"The controller {controller.name} added to inventory.\n")
        else:
            print(f"The controller {controller.name} is already in the inventory.\n")

    def add_mobile(self, mobile):
        if mobile.mobile_id not in self.mobiles:
            self.mobiles[mobile.mobile_id] = mobile
            print(f"The Mobile {mobile.name} added to inventory.\n")
        else:
            print(f"The Mobile {mobile.name} is already in the inventory.\n")

    def add_monitor(self, monitor):
        if monitor.monitor_id not in self.monitors:
            self.monitors[monitor.monitor_id] = monitor
            print(f"The Monitor {monitor.name} added to inventory.\n")
        else:
            print(f"The Monitor {monitor.name} is already in the inventory.\n")

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

myStore= Store()
myInventory = Inventory()



def cls(): 
    os.system('cls' if os.name=='nt' else 'clear')

def write_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data + '\n')

def read_from_file(filename):
    with open(filename, 'r') as file:
        f_contents = file.read()
        print(f_contents)

def get_input(prompt, validator=None):
    while True:
        try:
            value = input(prompt)
            if validator:
                return validator(value)
            return value
        except ValueError as e:
            print(f"Error: {e}")

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
    
    print("choose 1 to add another employee")
    print("choose any for main menu\n")
    choice = int(input("choice: "))
    if choice == 1:
        getEmployeeInfo()
    else:
        start()

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
    
    print("choose 1 to add another customer")
    print("choose any for main menu\n")
    choice = int(input("choice: "))
    if choice == 1:
        getCustomerInfo()
    else:
        start()

def toList():
    cls()
    print("press 1 to list games archives.")
    print("press 2 to list consoles archives.")
    print("press 3 to list laptops archives.")
    print("press 4 to list controllers archives.")
    print("press 5 to list mobiles archives.")
    print("press 6 to list monitors archives.")
    print("press 7 to list employees archives.")
    print("press 8 to list customers archives.")
    print("press 9 to list purchases archives.")
    print("press 10 to list PC's archives")
    print("press 11 for main menu\n")
    choice = int(input("Choice: "))
    cls()
    
    if choice == 1:
        read_from_file('games.txt')
        pause()
    elif choice == 2:
        read_from_file('consoles.txt')
        pause()
    elif choice == 3:
        read_from_file('laptopes.txt')
        pause()
    elif choice == 4:
        read_from_file('controlleres.txt')
        pause()
    elif choice == 5:
        read_from_file('mobiles.txt')
        pause()
    elif choice == 6:
        read_from_file('monitors.txt')
        pause()
    elif choice == 7:
        read_from_file('employees.txt')
        pause()
    elif choice == 8:
        read_from_file('customers.txt')
        pause()    
    elif choice == 9:
        read_from_file('purchases.txt')
        pause()
    elif choice == 10:
        read_from_file('PCs.txt')
        pause()
    else:
        start()

def addGame():
    cls()
    id = input("Game id: ")
    cls()
    name = input("Game name: ")
    cls()
    gener = input("Game gener: ")
    cls()
    price = input("Game price: ")
    cls()
    quantity = input("Quantity: ")
    cls()
    toAdd = Game(id, name, gener, price, quantity)
    myInventory.add_game(toAdd)
    print("choose 1 to add another game.")
    print("choose any for main menu.\n")
    choice = int(input("choice: "))
    if choice == 1:
        addGame()
    else:
        start()

def addConsole():
    cls()
    id = input("Console id: ")
    cls()
    name = input("Console name: ")
    cls()
    price = input("Console price: ")
    cls()
    quantity = input("Quantity: ")
    cls()
    toAdd = Console(id, name, price, quantity)
    myInventory.add_console(toAdd)
    print("choose 1 to add another console.")
    print("choose any for main menu.")
    choice = int(input("choice: "))
    if choice == 1:
        addConsole()
    else:
        start()

def addPC():
    cls()
    id = input("PC's id: ")
    cls()
    name = input("PC's name: ")
    cls()
    gpu = input("PC's GPU: ")
    cls()
    cpu = input("PC's CPU: ")
    cls()
    motherBord = input("PC's motherbord: ")
    cls()
    price = input("PC's price: ")
    cls()
    quantity = input("Quantity: ")
    cls()
    toAdd = PC(id, name, gpu, cpu, motherBord, price, quantity)
    myInventory.add_PC(toAdd)
    print("choose 1 to add another pc.")
    print("choose any for main menu.\n")
    choice = int(input("choice: "))
    if choice == 1:
        addPC()
    else:
        start()

def addLaptop():
    cls()
    id = input("laptop id: ")
    cls()
    name = input("laptop name: ")
    cls()
    gpu = input("laptop GPU: ")
    cls()
    cpu = input("laptop CPU: ")
    cls()
    price = input("laptop price: ")
    cls()
    quantity = input("Quantity: ")
    cls()
    toAdd = Laptop(id, name, gpu, cpu, price, quantity)
    myInventory.add_laptop(toAdd)
    print("choose 1 to add another laptop.")
    print("choose any for main menu.\n")
    choice = int(input("choice: "))
    if choice == 1:
        addLaptop()
    else:
        start()

def purchase():
    cls()
    itemID = input("Item ID: ")
    cls()
    itemName = input("Item name: ")
    cls()
    customerPhoneNum = get_input("customer Phone Number: ", Validation.validate_phone)
    cls()
    today = date.today()
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    write_to_file('purchases.txt', f"Date: {today}\nTime: {current_time}\nItem ID: {itemID}\nitem name: {itemName}\nCustomer Phone Number: {customerPhoneNum}\n")
    print("The purchase is added to archives succesfully\n")
    print("choose 1 to make another purchase.")
    print("choose any for main menu.\n")
    choice = int(input("choice: "))
    if choice == 1:
        purchase()
    else:
        start()

def pause():
    pauser = input("Press enter to continue...")
    cls()
    print("choose 1 to open another archive.")
    print("choose any for main menu.\n")
    choice = int(input("choice: "))
    if choice == 1:
        toList()
    else:
        start()

def addMonitor():
    cls()
    id = input("Monitor id: ")
    cls()
    name = input("Monitor name: ")
    cls()
    size = input("Monitor size: ")
    cls()
    price = input("Monitor price: ")
    cls()
    quantity = input("Quantity: ")
    cls()
    toAdd = Monitor(id, name, size, price, quantity)
    myInventory.add_monitor(toAdd)
    print("choose 1 to add another monitor.")
    print("choose any for main menu.\n")
    choice = int(input("choice: "))
    if choice == 1:
        addMonitor()
    else:
        start()

def addMobile():
    cls()
    id = input("Mobile id: ")
    cls()
    name = input("Mobile name: ")
    cls()
    storage = input("Mobile storage: ")
    cls()
    price = input("Mobile price: ")
    cls()
    quantity = input("Quantity: ")
    cls()
    toAdd = Mobile(id, name, storage, price, quantity)
    myInventory.add_mobile(toAdd)
    print("choose 1 to add another mobile.")
    print("choose any for main menu.\n")
    choice = int(input("choice: "))
    if choice == 1:
        addMobile()
    else:
        start()

def addController():
    cls()
    id = input("controller id: ")
    cls()
    name = input("controller name: ")
    cls()
    price = input("controller price: ")
    cls()
    quantity = input("Quantity: ")
    cls()
    toAdd = Controller(id, name, price, quantity)
    myInventory.add_controller(toAdd)
    print("choose 1 to add another controller.")
    print("choose any for main menu.\n")
    choice = int(input("choice: "))
    if choice == 1:
        addController()
    else:
        start()


def start():
    cls()
    print("choose 1 to add a game.")
    print("choose 2 to add a console.")
    print("choose 3 to add a PC.")
    print("choose 4 to add a laptop.")
    print("choose 5 to add a controller.")
    print("choose 6 to add a mobile.")
    print("choose 7 to add a monitor.")
    print("choose 8 to add an employee.")
    print("choose 9 to add a customer.")
    print("choose 10 to list an archive.")
    print("choose 11 to make a purchase.")
    print("choose 0 to exit.\n")
    choice = int(input("choice: "))
    if choice == 1:
        addGame()
    elif choice == 2:
        addConsole()
    elif choice == 3:
        addPC()
    elif choice == 4:
        addLaptop()
    elif choice == 5:
        addController()
    elif choice == 6:
        addMobile()
    elif choice == 7:
        addMonitor()
    elif choice == 8:
        getEmployeeInfo()
    elif choice == 9:
        getCustomerInfo()
    elif choice == 10:
        toList()
    elif choice == 11:
        purchase()
    elif choice == 0:
        cls()
        quit()
    else:
        start()






