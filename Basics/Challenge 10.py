# Challenge 10
def NumbersSum(numbers):
    return sum(numbers)

numbers = []
for i in range(5):
    numbers.append(int(input("Give me a number one at a time: ")))

print(f"The sum of your numbers is: {NumbersSum(numbers)}")