num_1 = int(input("Please enter value for Number 1: "))
num_2 = int(input("Please enter value for Number 2: "))

# To swap the value of two variables  
# we will user third variable which is a temporary variable  
temp_1 = num_1
num_1 = num_2
num_2 = temp_1
print("==============================================")
print("The Value of Number 1 after swapping: ", num_1)
print("The Value of Number 2 after swapping: ", num_2)

# OR
print("==============================================")
num_1,num_2 = num_2, num_1

print("The Value of Number 1 after swapping: ", num_1)
print("The Value of Number 2 after swapping: ", num_2)

# OR
print("==============================================")
num_1 = num_1 + num_2
num_2 = num_1 -  num_2
num_1 = num_1 -  num_2

print("The Value of Number 1 after swapping: ", num_1)
print("The Value of Number 2 after swapping: ", num_2)
print("==============================================")