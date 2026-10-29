
# first_names = ["BlueRay ", "Upchuck ", "Lojack ", "Gizmo ", "Do-Rag "]

# last_names = ["Zzz", "Burp", "Dogbone", "Droop"]

# full_names = []

# i = 0

# for first in first_names:
#     for i in range(0, len(last_names), 1):
#         full_names.append(first + " " + last_names[i])
#         i = i + 1
#         break



# print(full_names)



# use of .lower() and .upper() and .title() methods
# first_name = "John"
# first_name_lower = first_name.lower()
# first_name_upper = first_name.upper()
# first_name_title = first_name.title()

# print("Lowercase:", first_name_lower)
# print("Uppercase:", first_name_upper)
# print("Title Case:", first_name_title)

# print("================================")

#Dictionary example
person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "city": "New York"
}

for i in person.keys():
    print(i, ":", person[i])

print("================================")


for i in person.values():
    print(i)


print("================================")


for key, item in person.items():
    print(key, ":", item)


print("================================")

#Simple function example
def display_result(winner, score):
    print("The winner was " + winner)
    print("The score was " + score)


#Optional Arguments
def display_result(winner, score, **other_info):
    print("The winner was " + winner)
    print("The score was " + score)
    for key, value in other_info.items():
        print(key + ": " + value)


display_result(winner="Real Madrid", score="1-0", overtime ="yes", injuries="none")


print("================================")



from Modules import calculations
tax_for_this_order = calculations.calc_tax(sales_total = 101.37, tax_rate = .05)
print("Tax for this order: $", tax_for_this_order)

























import csv
from pathlib import Path

with open(Path(__file__).parent / "competitions.csv") as f:
    contents_of_f = csv.reader(f)
    potter_competitions = []
    for each_line in contents_of_f:
        potter_competitions.append(each_line)
#we can add items in list by "+" operator, but it is not a good practice to use it in a loop. It is better to use the append() method of the list.


print(potter_competitions)



#CSV files: Picking information out of them
print(potter_competitions[3])

index_number_of_target = potter_competitions.index("Best-Kept Lawn")



target = input("Enter the name of a competition:")

index_number_of_target = potter_competitions.index(target)

index_number_of_winner = index_number_of_target + 1

the_winner = potter_competitions[index_number_of_winner]
print("The winner was " + the_winner)



#CSV files: Loading information into them.
with open(Path(__file__).parent / "competitions.csv", "a") as f:
    data_handler = csv.writer(f, delimiter=",")

    data_handler.writerow(["Year", "Event", "Winner"])
    data_handler.writerow(["1995", "Best-Kept Lawn", "None"])
    data_handler.writerow(["1999", "Gobstones", "Welch National"])


# CSV files: Appending rows to them
with open(Path(__file__).parent / "whatever.csv", "a", newline="") as f:
    data_handler = csv.writer(f, delimiter=",")

    data_handler.writerow(["2006", "World Cup", "Burkina Faso"])
    data_handler.writerow(["2011", "Butter Cup", "France"])
    data_handler.writerow(["2012", "Coffee Cup", "Brazil"])


# #without handler
# with open(Path(__file__).parent / "whatever.csv", "a", newline="") as f:
#     f.write("2013,Tea Cup,China\n")
#     f.write("2014,Water Cup,USA\n")