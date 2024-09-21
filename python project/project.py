class store :
    def __init__(self, name ):
        self.name = name
        self.inventory= inventory()
        self.customers= []
        self.orders=[]

    def add_customer(self, customer):
        self.customers.append(customer)

    def add_order(self,order):
        self.orders.append(order)

    def save_data(self):
        FileHandler.save_to_file('store_data.txt',self)

    def load_data(self):
        return
        FileHandler.load_from_file('store_data.txt')

class console:
    def __init__(self,model,brand,price):
        self.model=model
        self.brand=brand
        self.price=price
    def __str__(self):
        return f"{self.brand} {self.model} - ${self.price}"             

class game:
    def __init__(self,title,genre,price):
        self.title=title
        self.genre=genre
        self.price=price 
    def __str__(self):
     return f"{self.title} ({self.genre}) - ${self.price}"    
    
class customer:
    def __init__(self, id, name, address, phone):
        self.id=id
        self.name=name    
        self.address=address
        self.phone=phone
        phoneCheck.validate(phone)
        self.cart=shoppingcart(self)

    def add_to_cart(self,item):
        self.cart.add_item(item)

    def place_order(self):
        order=self.cart.checkout()
        return order        

class Order:
    def __init__(self, customer, items, total_cost, date):
        self.customer=customer
        self.items=items
        self.total_cost=total_cost
        self.date=date
    def __str__(self):
        return f"Order for {self.customer.name} on {self.date}:   {self.items}  Total: ${self.total_cost}"        

class phoneCheck:
    @staticmethod
    def validate(phone):
        if phone.startswith(('77','78','70','73','71')) and len(phone)==9:
            return phone    
        else:
            raise ValueError("Invalid phone number")
import json
class FileHandler:
    @staticmethod
    def save_to_file(filename, data):
        with open(filename,'w') as f:
            json.dump(data.__dict__,f)
    @staticmethod
    def load_from_file(filename):
        with open(filename,'r') as f:
            return json.load(f)

class shoppingcart:
    def __init__(self, customer):
        self.customer=customer
        self.items= []
    def add_item(self, item):
        self.items.append(item)
    def checkout(self):
        total_cost=sum([ item.price for item in self.items])
        order= Order(self.customer, self.items, total_cost, "2024-09-09")
        return order            

class inventory:
    def __init__(self):
        self.consoles= []
        self.games= []

    def add_console(self,console):
        self.consoles.append(console)

    def add_game(self, game):
        self.games.append(game)

    def list_consoles(self):
        return self.consoles                              
    
    def list_games(self):
        return self.games 

class billing:
    def __init__(self, order):
        self.order=order

    def generate_bill(self):
        print(f"Billing for {self.order.customer.name}: ${self.order.total_cost}")

class discount:
    def __init__(self,percentage):
        self.percentage=percentage

    def apply_discount(self, total_cost):
        return total_cost-(total_cost*self.percentage/100)

class OrderHistory:
    def __init__(self):
        self.history={}

    def add_order(self,customer,order):
        if customer.id not in self.history:
            self.history[customer.id]=[]

        self.history[customer.id].append(order)

    def get_order_history(self, customer):
        return self.history.get(customer.id,[])

if __name__=="__main__":
    store=store("Game Hub")

    console1=console("PS5","Sony",500)
    console2=console("Xbox","Microsoft",450)

    game1=game("FIFA 24","Sports",49)
    game2=game("Call Of Duty: MW3","War",39)

    store.inventory.add_console(console1)
    store.inventory.add_console(console2)

    store.inventory.add_game(game1)
    store.inventory.add_game(game2)

    customer1= customer(101,"Abdullah Mofudhal","Haddah ST.","779788788")

    customer1.add_to_cart(console1)
    customer1.add_to_cart(game1)
    order =customer1.place_order()

    store.add_order(order)

    store.save_data()

    store_loaded=store.load_data()
    print(store_loaded)