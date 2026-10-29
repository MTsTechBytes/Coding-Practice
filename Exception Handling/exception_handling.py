filename = input("What text file to open? ")
with open(filename) as f:
   print(f.read())

try:
   filename = input("What text file to open? ")
   with open(filename) as f:
     print(f.read())

except FileNotFoundError:
   print("Sorry, " + filename + " not found.")



#More practical way
while True:
    try:
        filename = input("What text file to open? ")
        with open(filename) as f:
            print(f.read())
            break

    except FileNotFoundError:
        print("Sorry, " + filename + " not found.")

