import os
#os.system('cls') => clears the screen on windows
os.system('clear') # => clears the screen on linux, os x

arr = (3,6,7,8,9) # array of numbes
decimal_array = (3.5, 6.7, 4.9, 10.2)
boolean_array = (True, False, True, False)
nameArray = ("Dunieski", "Megan", "Robert", "Blaine") # array of names

length = int(input("How many times do you want to print 'Student' >> "))
for s in range(length):
    print("Student")

floatNumer = int(input("Enter a decimal >> "))
sum = floatNumer + 4.6
print(sum)

print(4.6 + 2)

#length = len(arr)
#rint(f"The size of array arr is {length}")
# prints the elements in arr array
for i in range(len(arr)):
    print(arr[i])
    print("True")

print(arr)


