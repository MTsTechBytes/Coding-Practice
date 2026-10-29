c=10
d=11
x=1
y=3
a= 5
b = 4
g=8
h=9
f = 0


if c == d:

    if x == y:
        g = h
    elif a == b:
        g = h
    else:
        e = f
else:
    e = f








rankings = {
    5: "Finland", 
    2: "Norway", 
    3: "Sweden",
    7: "Iceland"
}

print(rankings[5])



country_ranks_so_far = {
    "Finland": 5, 
    "Norway": 2, 
    "Sweden": 3, 
    "Iceland": 7
}

print (country_ranks_so_far["Finland"])

print("================================")


info = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "country": "USA"
}

# we want to add new item to dict

info["email"] = "john.doe@example.com"

# now when we print the dict, it will include the new item
print(info)


#or
info.update({"phone": "123-456-7890"})


#Updating and removing items from a dictionary
info["age"] = 31  # Update age
#or
info.update({"age": 31})  # Update age

del info["city"]  # Remove city

#accessing dictionary items
print(info["name"])  # Access name
print(info.get("age"))  # Access age using get method



print("================================")

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


print("===============================================================================================================================")


# CREATING A LIST OF DICTIONARIES

deep_learning_models = [

    {
        "name": "ResNet",
        "epochs": 50,
        "accuracy": 0.75,
        "loss": 0.5
    },

    {
        "name": "VGG",
        "epochs": 100,
        "accuracy": 0.80,
        "loss": 0.4
    }, 

    {
        "name": "DEF",
        "epochs": 56,
        "accuracy": 0.85,
        "loss": 0.2
    }, 

    {
        "name": "AlexNet",
        "epochs": 75,
        "accuracy": 0.70,
        "loss": 0.5
    }, 


    {
        "name": "Inception",
        "epochs": 78,
        "accuracy": 0.90,
        "loss": 0.1
    }, 

]

print(deep_learning_models[3])

deep_learning_models.append(
                            {   
                                "name": "ABC",
                                "epochs": 80,
                                "accuracy": 0.60,
                                "loss": 0.7
                             }
                             
                            )

print(deep_learning_models)





best_model = deep_learning_models[0]

def best_deep_learning_model():
    global best_model

    for i in range(1, len(deep_learning_models), 1):

        if (deep_learning_models[i]["accuracy"] > best_model["accuracy"] ) and (deep_learning_models[i]["loss"] < best_model["loss"] ):

            best_model = deep_learning_models[i]


    return  best_model["name"]


print("Best model is ", best_deep_learning_model())

print("======================================================================================================")

















deep_learning_models = {

    "m1" : {
        "name": "ResNet",
        "epochs": 50,
        "accuracy": 0.75,
        "loss": 0.5
    },

    "m2" : {
        "name": "VGG",
        "epochs": 100,
        "accuracy": 0.80,
        "loss": 0.4
    }, 

    "m3" : {
        "name": "DEF",
        "epochs": 56,
        "accuracy": 0.85,
        "loss": 0.2
    }, 

    "m4" : {
        "name": "AlexNet",
        "epochs": 75,
        "accuracy": 0.70,
        "loss": 0.5
    }, 


    "m5" : {
        "name": "Inception",
        "epochs": 78,
        "accuracy": 0.90,
        "loss": 0.1
    }, 

}


print(deep_learning_models["m1"]["name"])



print("================================")



customer_29876 = {
    "first name": "David",
    "last name": "Elliott",
    "address": "4803 Wellesley St.",
    "discounts": ["standard", "volume", "loyalty"]
}


if "volume" in customer_29876["discounts"]:
    print("Customer 29876 has a volume discount.")




print(customer_29876["discounts"][1])





print("======================================================================================================")


def sum(a, b=20):
    print("Sum is:", a + b)


sum(5)

#OR

sum(a=5)





print("================================")

#Simple function example
def display_result(winner, score):
    print("The winner was " + winner)
    print("The score was " + score)




#Optional Arguments
def display_result(winner, score,                        **other_info):
    print("The winner was " + winner)
    print("The score was " + score)

    for key, value in other_info.items():
        print(key + ": " + value)


display_result(winner="Real Madrid", score="1-0",     overtime ="yes", injuries="none")



# optional arguments are printed as tuples when using *args, and as a dictionary when using **kwargs.
def display_nums(first_num, second_num, *opt_nums):
    print(first_num)
    print(second_num)
    print(opt_nums)

    return opt_nums

print(display_nums(100, 200, 300, 400, 500))

print("================================")




def add(num1, num2):
    return num1 + num2

result = add(num1 = 5, num2 = 10)
print(result)



#FUNCTION in a function

def now_say_something(what_to_say):
    print(what_to_say)


def say_something():
    what_to_say = "Hello, World!"
    now_say_something(what_to_say)

say_something()


print("=================================================================================================================")

# WHILE Loop


cont = ""

while True:

    cont = input("Enter Y to continue or N to stop")

    if cont != "N":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("Sum:", num1+num2)
    else:
        break
    
print("=================================================================================================================")











