import random

class Bankster:
    def __init__(self, name, gender, acct_num, balance, taxi_budget):
        self.name = name
        self.gender = gender
        self.acct_num = acct_num
        self.balance = balance
        self.taxi_budget = taxi_budget

    def debit(self, amount):
        self.balance -= amount

    def credit(self, amount):
        self.balance += amount

    def add2_taxi_budget(self, amount):
        self.taxi_budget += amount

john = Bankster("John", "m", 12345, 1000, 0)
jane = Bankster("Jane", "f", 12346, 1000, 0)

customers = [john, jane]

def random_walk(n):
    x, y = 0, 0
    for i in range(n):
        dx, dy = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x += dx
        y += dy
    return x, y

for i in range(5):
    walk = random_walk(30)
    customer = random.choice(customers)
    dist = abs(walk[0]) + abs(walk[1])
    dist_message = "{} went {} blocks.".format(customer.name, dist)
    taxi_fare = 4.5 + (.2 * dist)
    taxi_message = "{} needs a taxi. The taxi cost ${}.".format(customer.name, taxi_fare)
    hoof_it = "{} will walk.".format(customer.name)
    if dist >= 5:
        customer.debit(taxi_fare)
        customer.add2_taxi_budget(taxi_fare)
        print(walk, dist_message, taxi_message)
    else:
        print(walk, dist_message, hoof_it)

for c in customers:
    if c.gender == "m":
        print("Taxis cost {} ${} today. His bank account now has ${}.".format(c.name, c.taxi_budget, c.balance))
    else:
        print("Taxis cost {} ${} today. Her bank account now has ${}.".format(c.name, c.taxi_budget, c.balance))
