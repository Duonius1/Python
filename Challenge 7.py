# Challenge 7
# Declaring starting numbers + counter for Fibonacci sequence
num1 = int(0)
num2 = int(1)
counter = int(1)
print (0, end = "", sep = ", ") # The first two numbers of the Fibonacci sequence
while (counter <10):
    sum = int(num1 + num2)
    print (", ", sum, end = "", sep = "")
    num2 = num1
    num1 = sum
    counter += 1

'''
# Alternative (and much simpler) way to do it:
for i in range(10):
    print(a) # Prints in new line every time though, but is better in general
    a, b = b, a + b
'''