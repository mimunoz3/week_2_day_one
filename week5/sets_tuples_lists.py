# collection =single "variable" used to store multiple values

# list = [] ordered and changeab;e, dublicates OK
# fruits =["apple", "orange", "banana", "coconut", "kiwi", "strawberry"]
# print(dir(fruits))
#print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# set = {} unordered and immutable, but Add/Remove OK. NO dublicates
#fruits = {"apple", "orange", "banana", "coconut"}
#print(fruits)
#print(dir(fruits))
#print(len(fruits))
#promt("pineapple" in fruits)
# print(fruits[0]) - gives an error because a set has no order, it is not a list
#fruits.add("pineapple")
#fruits.add("strawberry")
#fruits.remove("apple")
#fruits.pop()
#fruits.clear()
#print(fruits)

# tuple = () ordered and unchangeable. Duplicates OK. FASTER
#fruits = ("apple", "orange", "banana", "coconut")
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("pineapple" in fruits)
#print(fruits.index("apple"))
#print(fruits.count("cocounut"))
#print(fruits)
#for fruit in fruits:
#    print(fruit)

# dictionary - a collection of {key:value} pairs ordered and changeable. No duplicates
# capitals = {"USA":"Washington D.C.",
#            "India": "New Delhi",
#            "China": "Beijing",
#            "Russia": "Moscow"}
##print(dir(capitals))
#print(help(capitals))
#print(capitals.get("USA"))
#if capitals.get("India"):
    #print("That capital exists")
#else:
#    print("That capital doesn't exist")
#capitals.update({"Germany": "Berlin"})
#capitals.update({"USA": "Detroit"})
#print(capitals)
#capitals.pop("China")
#capitals.popitem()
#capitals.clear

#keys = capitals.keys()
#print(keys)
#for key in capitals.keys():
#    print()

#values = capitals.values()
#for value in capitals.values():
#   print(value)

#items = capitals.items()
#for key, value in capitals.items():
#    print(f"{key}: {value}")

# you can reassign value using this:
# fruits[1] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0,"pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()

# print(fruits[0:3])
# for fruit in fruits:
# print(fruit)

#cars = ["bmw", "maserati", "audi", "mercedes", "ferrari"]
#print(f"these are list of {cars}")
#print(f"the first car is {cars[0]}")

# changing the value of the list
#cars[0] = "toyota"
#print(f"is the last car is {cars[-1]}")
#cars[-1] = "lamborghini"
#print(f"the last car is {cars[-1]}")

#adding a new value to the list
#cars.append("bugatti")
#print(cars)
#cars.remove("maserati")
#print(cars)

# looping through the list otherwise called iterating through the list

#for car in cars:
#print(len(car))
#print(car)

#carRequest = input("add a new car please: ")
#cars.append(carRequest)
#print(cars)
#print(len(cars))
#print(cars.upper())
#print(cars)
#if len(cars) > 10: 
#break


# challenge
# create a list of friends 
# make sure the initial list is 0 
#friends = []
# add a new friend to the list, add at least 5
#friends.append("lesly")
#friends.append("maggie")
#friends.append("abby")
#friends.append("Julian")
#friends.append("vivi")
#print(friends)
# remove a friend 
#friends.remove("Julian")
# insert a friend at a specidic index, 2
#friends.insert(2, 'Noelia')
# print the list of friends 
#print(friends)
# loop through the list and print the friends name
# for friend in friends:
 #   print(len(friends))
 #   print(friend)

# see if a particular friend is in the list (boolean value)
#print("Xavier" in friends)
# if the list is greater than 10 break the loop
#if len(cars) > 10:
 #   break