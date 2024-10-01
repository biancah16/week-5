#collection = single "variable" used to store multiple values
#lists = [] ordered abd changeable. duplicates OK
# #set = {} unordered and immutable, but Add/remove OK No duplicates
# #tuples  () ordered and unchangeable . duplicates OK FASTER
# fruits = ["apple" ,  "orange" , "banana" , "coconut" , "strawberry" , "kiwi" , "mango"]
# # print(fruits[::2]) #gives you every second element
# # print(fruits[::-1]) #gives you the elements backwards
# #print(fruits[0])
# #for fruit in fruits:
#       #print(fruit)
# for fruit in fruits:
#       print(fruit)

# #control question mark makes a comment
# # print(dir(fruits)) #dir gives you all the attributes of a list, what it can do
# # print(help(fruits))
# # print(len(fruits)) # gives you the lenth / counts
# # print("pineapple" in fruits) # says if it is in the list
# # fruits[0] = "pineapple"
# # fruits[1] = "apple"#changes the value
# # fruits.append("pineapple") adds to the end of your list
# # # fruits.remove("apple") speaks for itsself lol
# # fruits.insert(0,i
#"pineapple")puts everything there and push everything else
# #fruits.sort() puts in alphabetical order
# # fruits.reverse() speaks for itself
# # fruits.clear() removes everything
# print(fruits.index("apple")) #finds the  index of the elements
# print(fruits)


# cars = ["ford", "volvo" , "BMW"]
# #add 4 new cars in the list
# cars.append("honda")
# #print out the list of cards in an f-string
# #that says "the cars in the list are:"
# print(cars)
# print(f"the cars in this list are: {cars}")
# #replacde the last element in the list with another car
# cars[-1] = "austin martin"
# #print out the list of cards in an f string

# #add 4 more cars
# # # print(cars.append)("honda")
# # print(cars.append)("toyota")
# # print(cars.append)("tesla")
# # print(cars.append)("voltswagon")
# # print(list)
# #replace the third element in the list with another car
# #print out the list of cars in an f-string
# print(f"{cars}")
# #insert a new car in the sencond position
# #print our the list of cars in an f-string
# newCars= ["ford", "tesla" , "BMW", "volvo"]
# print(f"{newCars}")
# #remove the thrid element of the list
# #print out the lift of cars in an f-string'

# #check is the lift contains the car "ford"
# #print our the result in an f-string
# for car in cars:
#     requestCar = input("enter a car: ")
#     cars.append(requestCar)
#     print(f'the cars in the list are:{cars}')
#     # if len(cars) ==10:
#     # print("you have reached the maximum number of cars")
#     # break

#challenge😥😪
#create a list of friends
friends =["skibiti" , "john pork"]
#add 4 new friends in the list
print(friends.append("new character"))
print(friends.append("elsa"))
print(friends.append("gmail dog"))
print(friends.append("diddy"))
#print out the list of friends in an f-string'
print(f"{friends}")
#replace the last element in the list with another friend
friends[-1] = "orange cat"
#print out the list of friends in an f-string'
print(f"{friends}")
#replace the 3rd element in the list with another firend
friends[2] = "savesta"
#print out the list of friends in an f-string'
print(f"{friends}")
#insert a new friend in the second position
friends[1] = "kumalalala"
#print out the list of friends in an f-string'
print(f"{friends}")

##########sets#########
# sets are unordered and unindexed
# they are defined using curly brackets
# they do notallow duplicates
fruits = {"apple" , "banana" , "mango" , "cherry" , "watermelon"}
print (fruits)
# print(dir(fruits)) # methiods that can be used with sets
# print(help(fruits)) #documentation / methods that cab ve used with sets
# # print(len(fruits))#number if ekements in the set
# print("volvo" in fruits) #check if an element is in the set
# add an elemnt ti the set
# print(fruits.add("orange"))
# print(fruits)
# print(fruits.add("kiwi"))
# print(fruits)
#add multiple elemets to the set
print(fruits.update(["orange" , "kiwi" , "pineapple"]))
print(fruits)
print(fruits.pop()) #removes the last elemnt in the set
print(fruits)
print(fruits.clear())#clears the set
print(fruits)
#when to use sets:
#sets are useful whjen you wan t to store a 
#collection of items that should not be chnaged
#and you do not crae about the order of the items
#example:a collection of unique items
social_security_numbers = {123456789 , 987654321, 123456789}
#remove the last element in this set
# print(social_security_numbers.pop()) 
print(social_security_numbers)
#add another social security  number\
print(social_security_numbers.add(345678901))
print(social_security_numbers)
social_security_numbers.add(123456789)
print(social_security_numbers)





###########tuples#########
#tuples are immutable and are defined using parenthesis
#create a tuple ckaked my_tuple with the following values
example_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(example_tuple)
# print(example_tuple.count(2))#count the number of times tghe value 2 appears in the tuple
# print(dir(example_tuple))#attribvutes that can be used with tuples
# print(help(example_tuple)) # document/ methods that can be used with tuples
# print(len(example_tuple))#number of elemnts in the suple
# print(2 in example_tuple) # check ifd an elemnt in in the tuple
# #When are they usefull?????🤔
# #if you want to find the index of a value in a tuple
# print(example_tuple.index(2))
# lymeric = "peter pipe picked a peck of pickled peppers peppers"
# #convert the strring to a tuple
# #split it first
# lymeric_tuple = tuple(lymeric.split())
# print(lymeric_tuple)
# #find howe many times peck appears
# print(lymeric_tuple.count())

#loops with tuples
for item in example_tuple:
    print(item)

    ##########dictionary##########
#dictrionaries are unordered , chnageaoke and indexed
    #tbeg are defines using curly brACVKETS
    #they have keys anf vlauers
#a collectionj of {key:value} pairs, no duplicates
    #keys are unque
    #values can be of any data type

capitals = {"Kenya":"Nairobi",
             "Uganda": "kampala",
             "Tanzania":"Dodoma",
             "Rwanda":"Kingali",
             "China": "Beijing",
             "USA":"Washington DC"}
print(capitals)
print(dir(capitals))#attributes thqt can be used with dictionaries
print(help(capitals))#documentation / methods thast can bve used with dictionaries
print(len(capitals)) #number of itens in the digtionaru
#if you  want to check the value of a key in the dictionary
print(capitals["Kenya"])
print(capitals.get("Kenya"))
#add an item to the dictionary
capitals["South Africa"] = "Pretoria"
print(capitals)
capitals.update({"Nigeria":"Abuja"})
#add three more contries and trhier capitals to the dictonary
capitals.update({"France" : "paris", "Germany":"Berlin", "Italy": "Rome"})
capitals.pop("China")#remover an item form the dictionary
print(capitals)
#clear the dictionary 
#capitals.clear(#do not run this
# loop through the dicitonary to gety the keys
for key in capitals:
    print(f"these are the {key}")

#print the vaklured in the dictioanry
for value in capitals.values():
    print(value)

    #print tge jey value pairs in trhe dictionary
items_all = capitals.items() #key value pairs
for key, value in items_all:
    print(f"{key}is the capital of {value}")

                              
