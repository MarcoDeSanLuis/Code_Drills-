#random_walk.rb 

class Bankster 
	attr_accessor :name, :gender, :acct_num, :balance, :taxi_budget
	def initialize(name, gender, acct_num, balance, taxi_budget)
		@name = name
		@gender = gender
		@acct_num = acct_num 
		@balance = balance 
		@taxi_budget = taxi_budget
	end 
	def debit(amount) 
		self.balance -= amount
	end 
	def credit(amount) 
		self.balance += amount 
	end 
	def add2_taxi_budget(amount)
		self.taxi_budget += amount 
	end
end 	
	
john = Bankster.new("John", "m", 12345, 1000, 0) 
jane = Bankster.new("Jane", "f", 12346, 1000, 0) 

customers = [john, jane]

def random_walk(n) 
	x, y = 0,0
	for i in (n) 
		directions = ['n', 's', 'e', 'w']
		step = directions.sample 
		if step == 'n' 
			y += 1 
		elsif step == 's'
			y -= 1 
		elsif step == 'e'
			x += 1 
		else 
			x -= 1 
		end 
	end 
	return x, y 
end 

for i in (1..5)
	walk = random_walk(1..30)
	customer = customers.sample 
	dist = walk[0].abs + walk[1].abs
	dist_message = " #{customer.name} went #{dist} blocks." 
	taxi_fare = 4.5 + (0.02 * dist) 
	taxi_message = " #{customer.name} needs a taxi. The taxi costs $#{taxi_fare}."
	hoof_it = " #{customer.name} is going to walk."
	if dist >= 5 
		customer.debit(taxi_fare)
		customer.add2_taxi_budget(taxi_fare) 
		print walk, dist_message
		puts taxi_message
	else 
		print walk, dist_message
		puts hoof_it
	end 
end 

customers.each do |c|
	if c.gender == 'm'
		puts "Taxis cost #{c.name} $#{c.taxi_budget} today. His bank account now has $#{c.balance}."
	else 
		puts "Taxis cost #{c.name} $#{c.taxi_budget} today. Her bank account now has $#{c.balance}."
	end 
end
