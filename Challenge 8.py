# Challenge 8
# List of my favorite fruits
Fruits = ["Orange", "Banana", "Cherry", "Apple", "Mango"]

Fruit = (input("What is your favorite fruit? "))

if Fruit in Fruits: # "in" is very useful for finding stuff in lists
    print("We both love ", Fruit, "!", sep = "")
else:
    print("I Haven't tried ", Fruit, " yet. I'll have to give it a go!", sep = "")