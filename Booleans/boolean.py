import os
os.system("clear")

isFromNCI = False # flag

name = input("Enter a name >> ")
if (name == "Robert" or name == "Blaine"):
    isFromNCI = True
else:
    isFromNCI = False

if(isFromNCI):
    print(f"{name} studies at NCI")
else:
    print(f"{name} does not study at NCI")