import calculate_percentage

obt_marks = int(input("Enter your obtain marks: "))
total_marks = int(input("Enter your total marks: "))

percentage = calculate_percentage.calculate_percentage(obt_marks, total_marks)
print("Your percentage is: ", percentage)