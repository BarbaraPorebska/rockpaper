'''
2. Password generator
In this project you will write your own password generator. Program asks the user to input password lenght. Then generate random passwords with lower case letters, upper case letters, digits and special characters. In the basic version you don't don't have to worry about whether your randomly generated password contains at least one character from every set, but you can also think about how to do it!

Hints:
Object string has builded-in constance strings you can use in your program:
string.ascii_letters # Concatenation of the ascii (upper and lowercase) letters
string.ascii_lowercase # All lower case letters
string.ascii_uppercase # All Upper case letters
string.digits  # The string ‘0123456789’.
string.punctuation  # String of ASCII characters which are considered special characters.

You can concatenated strings you need and choose a random character using:
random.choice(string_with_all_characters)
'''

import random
import string

#let’s greet the user!
print('Serdecznie witamy w naszym generatorze!') 

#Next, let’s ask the user for the length of the password.
length = int(input("Jak długie hasło Państwo sobie życzą? ")) 
#odejmujemy 4 znaki, z których każdy jeden ma być różnego rodzaju:
length2 = length - 4 


#Its time to define the data. We will make use of string module for the same.
#Concatenation of the ascii (upper and lowercase) letters
string.ascii_letters
#All lower case letters
lower = string.ascii_lowercase 
#All Upper case letters
upper = string.ascii_uppercase 
#The string ‘0123456789’.
num = string.digits 
#String of ASCII characters which are considered punctuation characters in the C locale.
symbols = string.punctuation 

#przypisywanie po jednym losowym znaku (argumenty funkcji to lista, ilość z próbki)
lower2 = random.sample(lower,1)
upper2 = random.sample(upper,1)
num2 = random.sample(num,1)
symbols2 = random.sample(symbols,1)

#w zmiennej łączymy te elementy, które muszą być po jednym:
at_least_one = lower2 + upper2 + num2 + symbols2

#w zmiennej łączymy te elementy, które muszą być po jednym:
string_with_all_characters = lower + upper + num + symbols 

#w kolejnej zmiennej zapisujemy 4 elementy w których musi by
temp2 = random.sample(at_least_one,4)
#Now that we have the data, let’s make use of random module to finally generate the password.
temp = random.sample(string_with_all_characters,length)
password = "".join(temp)
#We are passing in the combined data along with the length of the password, and joining them at the end.

#Finally, let’s print the password!
print(password)

