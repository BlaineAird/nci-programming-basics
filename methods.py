
# A simple menthod

def printName():
    print("My name is Dunieski") # this is a string
    print(4 + 7 - 3 * 5) 
    # 4 + 7 - 15
    # 11 - 15
    # - 4
    print(10 % 4)
    print(10 / 4)
    # first multiplication *
    # then division /
    # then modulus % => finds the remainder
    # addition +
    # substraction -

    name = input("Enter your name >> ")
    lname = input("Now, enter your last name >> ")
    text = "How are you ?"
    # highly recommended
    print("Welcome, {0} {1}. {2}".format(name, lname, text))
    # less secure
    print(f"Welcome, {name} {lname}, {text}")
    
    # ******** Linux Examples ********
    # echo "Welcome, $name $lname, $text" => linux example
    # printf => linux example
    # *********************************

    # Useful info
    # Old '%s %s' % ('one', 'two')
    # New '{} {}'.format('one', 'two')
    # Old '%d %d' % (1, 2)
    # New '{} {}'.format(1, 2)
    # New '{1} {0}'.format('one', 'two')
    concate = "Dunieski" + " Otano" + "7" # => prints Dunieski Otano7
    print(concate)

printName() # => calling printName() method
# intellisense will tell you
