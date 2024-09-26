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