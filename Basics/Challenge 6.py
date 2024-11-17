# Challenge 6
# Declaring int for Challenge 6
UserNumber = int(input("Write a random number: "))

# While loop to count down to 0
for i in range(UserNumber, -1, -1):
    if i == 0:
        print(i, end="")  # No comma after the last number, Default is \n
    else:
        print(i, end=", ")