# Simple Password Generator Side Project
# Nicole Baez Espinosa
# Original project was done in C, this version is done using Python

# Random library is called
import random 



# This function generates the password
def gen_password(n, list_d, list_l, list_u, list_s):
   
   # A list is created to store the password
    password = []

   # Iterates through n to determine the type of character to be used
    for i in range(n):
        char_type = random.randint(0, 3) # Range is up to three since there are only 4 types of characters

        if char_type == 0:
            # Digit will be added to the password list
            password.append(random.choice(list_d))

        elif char_type == 1:
            # Lowercase letter will be added to the password list
            password.append(random.choice(list_l))

        elif char_type == 2:
            # Uppercase will be added to the password list
            password.append(random.choice(list_u))

        else:
            # Symbols will be added to the password list
            password.append(random.choice(list_s))

    string = '' # String literal variable is created to turn the list into a string
    
    for n in password: # Iterates through the password list and concatenates elements
        string += n

    return string # Returns password as a string

# This function turns the string literals into lists
def splice_lists(n):

    return n.split("#")


def main():
    # Takes in user input
    length = int(input("Enter password length: "))


  

   # Checks if password length is appropriate
    if length <= 0:
        print("Password is not long enough. Please try again.")
        

    # String literals are created and separated by '#'
    digits = '1#2#3#4#5#6#7#8#9'
    list_d = []
    list_d = splice_lists(digits) #splice_lists function is called and result is stored in a list
    

    lowers = 'a#b#c#d#e#f#g#h#i#j#k#l#m#n#o#p#q#r#s#t#u#v#w#x#y#z'
    list_l = []
    list_l = splice_lists(lowers)
   

    uppers = 'A#B#C#D#E#F#G#H#I#J#K#L#M#N#O#P#Q#R#S#T#U#V#W#X#Y#Z'
    list_u = []
    list_u = splice_lists(uppers)
    

    symbols = '!#@###$#%#^#&#*#(#)'
    list_s = []
    list_s = splice_lists(symbols)
    
    # Variable stores result from gen_password function
    password = gen_password(length,list_d,list_l, list_u, list_s)

    print("Password:", password)

main()