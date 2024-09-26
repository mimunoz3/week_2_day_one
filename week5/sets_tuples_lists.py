# collection =single "variable" used to store multiple values
# list = [] ordered and changeab;e, dublicates OK
# set = {} unordered and immutable, but Add/Remove OK. NO dublicates
# tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits =["apple", "orange", "banana", "coconut", "kiwi", "strawberry"]

# print(dir(fruits))
#print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# you can reassign value using this:
# fruits[1] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0,"pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()

# print(fruits[0:3])
for fruit in fruits:
print(fruit)