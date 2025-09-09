#Basic Function
def greet_user():
    """Display a simple greeting."""
    print("Hello!")
greet_user()
#Function Passing Information
def greet_user(username):
    print(f"Hello, {username.title()}!")
greet_user('jesse')
#Positional Arguments
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')
describe_pet('snake', 'ophelia')
#Printing not knowing 
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')