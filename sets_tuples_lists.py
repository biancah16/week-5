#collection = single "variable" used to store multiple values
#lists = [] ordered abd changeable. duplicates OK
#set = {} unordered and immutable, but Add/remove OK No duplicates
#tuples  () ordered and unchangeable . duplicates OK FASTER
fruits = ["apple" ,  "orange" , "banana" , "coconut" , "strawberry" , "kiwi" , "mango"]
# print(fruits[::2]) #gives you every second element
# print(fruits[::-1]) #gives you the elements backwards
#print(fruits[0])
#for fruit in fruits:
      #print(fruit)
for fruit in fruits:
      print(fruit)

#control question mark makes a comment
# print(dir(fruits)) #dir gives you all the attributes of a list, what it can do
# print(help(fruits))
# print(len(fruits)) # gives you the lenth / counts
# print("pineapple" in fruits) # says if it is in the list
# fruits[0] = "pineapple"
# fruits[1] = "apple"#changes the value
# fruits.append("pineapple") adds to the end of your list
# # fruits.remove("apple") speaks for itsself lol
# fruits.insert(0,"pineapple")puts everything there and push everything else
#fruits.sort() puts in alphabetical order
# fruits.reverse() speaks for itself
# fruits.clear() removes everything
print(fruits.index("apple")) #finds the  index of the elements
print(fruits)