num = 14 # num que eu quero transformar 
restos = [] # lista que armazena os resto da divisao
while num > 0: 
    restos.append(num % 2) # adiciona os restos (formula em parentesis) da divisão na lista
    num = num // 2 # configura que o dividendo sera sempre igual ao quoeficiente anterior, desde que não seja 0


binario = restos[::-1] # inverte a ordem da lista
print(binario) # mostra o resultado na tela

# Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user. Create several instances representing different users, and call both methods for each user.
class User:
    def __init__(self, first_name, last_name, age, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.birthday = birthday
    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Birthday: {self.birthday}")
    def greet_user(self):
        print(f'Hello, {self.first_name}, nice to see you')
for i in range(1, 3):
    first_name = input(f'Enter user {i} first name: ')
    last_name = input(f'Enter user {i} last name: ')
    age = int(input(f'Enter user {i} age: '))
    birthday = input(f'Enter user {i} birthday: ')
    print('=-'*50)
    user = User(first_name, last_name, age, birthday)
    print(f'User {i} data: {user.first_name} {user.last_name}, {user.age} years old and born on {user.birthday}')
    print('=-'*50)
    user.greet_user() 
    
