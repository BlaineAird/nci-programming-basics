
import os
os.system("clear")

def add(n1, n2):
    sum = n1 + n2   
    return sum

def substract(n1, n2):
    sub = n1 - n2
    return sub

def multiply(n1, n2):
    mul = n1 * n2
    return mul

def divide(n1, n2):
    try: # try - except used to handle exceptions
        div = n1 / n2 # if n2 is 0, exception is caught
    except ZeroDivisionError: return f"Not possible division by {n2}"
    return div

def modulus(n1, n2):
    try: # try - except used to handle exceptions
        mod = n1 % n2 # if n2 is 0, exception is caught
    except ZeroDivisionError: return f"Not possible division by {n2}"
    return mod


# Accepting input from users
num1 = int(input("Enter number 1 >> "))
num2 = int(input("Enter number 2 >> "))

addition = add(num1, num2)
substraction = substract(num1, num2)
multiplication = multiply(num1, num2)
division = divide(num1, num2)
modul = modulus(num1, num2)

print("Addition = {}".format(addition))
#print(f"Addition = {addition}")
print("Substraction = {}".format(substraction))
#print(f"Substraction = {substraction}")
print("Multiplication = {}".format(multiplication))
#print(f"Multiplication = {multiplication}")
print("Division = {}".format(division))
#print(f"Division = {division}")
print("Modulus = {}".format(modul))
#print(f"Modulus = {modul}")



phone = input("Enter your phone >> ")
print(f"Phone = {phone}")


studentName = input("What is your name? >> ")
print("Welcome, {}". format(studentName))

def personInfo(name, lname, age, phoneNum, PIN, school):
    print(f"""
    First Name:.............{name}
    Last Name:..............{lname}
    Age:....................{age}
    Phone:..................{phoneNum}
    PIN:....................{PIN}
    School:.................{school}
    """)

# starts here
os.system('clear')
print("******** Multiple Values for Function **********")
name = input("What is your first name? >> ")
lname = input("What is your last name? >> ")
age = input("What is your age? >> ")
phone = input("What is your phone? >> ") 
pin = input("What is your PIN? >> ")
school = input("What is your school? >> ")

personInfo(name, lname, age, phone, pin, school)

#array = ("Dunieski", "Otano", 44, "NCI", 1465, 34.2, True)

#index =>  0    1    2   3    4    5    6 => size - 1 
array1=[   87,  10,  2,  46,  22,  19,  66 ]# => size is 7
#size =>   1    2    3   4    5    6    7

cars = ["BMW", "Toyota", "Mercedes"]
cars.sort()
print(cars)


numbers = [6, 3, 8, 1, 2, 8, 3]
numbers.sort()
print(numbers)