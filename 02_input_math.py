#Comment your code (ie: # this is a comment)
#User input can be stored in variables and then manipulated
#We can use the 'dot format' method to control exactly how our output appears.
#If you enter text when a number is expected, the program will crash 
#(unless you implement code to handle the error correctly)

# get input

# ask user for name
name = input("What is your name? ")

# greet user and display math
print('Hello')
print("Hello", name)

# ask user for two numbers
num_1 = int(input("What is your favourite number? "))
num_2 = int(input("What is your second favourite number?"))

# add numbers together
add = num_1 + num_2

# multiply numbers together
multi = num_1 * num_2

# greet user and display math
print("Hello", name)
print("{} + {} = {}".format(num_1, num_2, add))
print(f'{num_1} * {num_2} = {multi}')
#print(f'{num_1} * {num_2} = {multi}')