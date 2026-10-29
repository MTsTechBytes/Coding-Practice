import csv

with open("competitions.csv", "r") as f:
    contents_of_f = csv.reader(f)

    potter_competitions = []

    for each_line in contents_of_f:
        potter_competitions.append(each_line)
#we can add items in list by "+" operator, but it is not a good practice to use it in a loop. It is better to use the append() method of the list.

print(potter_competitions)



#CSV files: Picking information out of them
print(potter_competitions[3])

index_number_of_target = potter_competitions.index("Best-Kept Lawn")
#OR
target = input("Enter the name of a competition:")
potter_competitions.index(target)

index_number_of_winner = index_number_of_target + 1

the_winner = potter_competitions[index_number_of_winner]
print("The winner was " + the_winner)




#CSV files: Loading information into them.
with open("competitions.csv", "w") as f:
    
    data_handler = csv.writer(f, delimiter=",")

    data_handler.writerow(["Year", "Event", "Winner"])
    data_handler.writerow(["1995", "Best-Kept Lawn", "None"])
    data_handler.writerow(["1999", "Gobstones", "Welch National"])





# CSV files: Appending rows to them
with open("whatever.csv", "a", newline="") as f:
    data_handler = csv.writer(f, delimiter=",")

    data_handler.writerow(["2006", "World Cup", "Burkina Faso"])
    data_handler.writerow(["2011", "Butter Cup", "France"])
    data_handler.writerow(["2012", "Coffee Cup", "Brazil"])


# #without handler
# with open(Path(__file__).parent / "whatever.csv", "a", newline="") as f:
#     f.write("2013,Tea Cup,China\n")
#     f.write("2014,Water Cup,USA\n")