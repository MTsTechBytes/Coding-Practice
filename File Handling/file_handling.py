# by using the with statement, we don't have to worry about closing the file
with open("whatever.txt", "w") as file_to_work_with:
    file_to_work_with.write("Hello World!\n")




# if we want to close the file, we won't use with
file_to_work_with = open("whatever.txt", "r")
print(file_to_work_with.read())
file_to_work_with.close()


print("==============================================")

greeting = "Hello, World!"

with open("greet.txt", "w") as f:
    f.write(greeting)


print("==============================================")
#read mode is default, so we don't have to specify it

with open("greet.txt", "r") as f:
    text_of_file = f.read()

print(text_of_file) 

print("==============================================")
#append mode is used to add content to the end of the file without overwriting it

with open("greet.txt", "a") as f:
    f.write("\nHave a nice day.")


with open("greet.txt", "r") as f:
    message = f.read()
    print(message)
