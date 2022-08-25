import random
import string
# it's nice to have your constants up top and in CAPS
SYMBOLS = ['!', '@', '#', '-', '@', '+', '%']
# it's easy to just omit '5' from a list of numbers
# easier to just have the list already be strings than mess around with ints
NUMBERS = ('0', '1', '2', '3', '4', '6', '7', '8', '9')
# quick list comprehension to omit 'e' and 'E'
LETTERS = [char for char in string.ascii_letters if char != 'e' and char != 'E']

length = int(input("Jak długie hasło Państwo sobie życzą? "))

# put all our logic in a function - def jest po to, żeby wziąć cały wycinek kodu i odwołać się do niego później jak tu na końcu create_password_insecure()
def create_password_insecure():
    # pick a symbol
    chosen_symbol = random.choice(SYMBOLS)
    # pick a number
    chosen_number = random.choice(NUMBERS)
    # pick some letters to fill out our 6-10 chars
    # we pick 4-8 not 6-10, since 2 chars will be symbol/number
    number_of_letters = random.randint(1, 9)
    # quick list comprehension to pick our letters
    chosen_letters = [random.choice(LETTERS) for i in range(number_of_letters)]
    # get all our elements in a single list
    password_elements_list = [chosen_symbol] + [chosen_number] + chosen_letters
    # (pseudo)randomize the list
    random.shuffle(password_elements_list)

    pseudorandom_password = ''.join(password_elements_list)
    print (pseudorandom_password)

create_password_insecure()