#Asking user for two numbers (as strings)
num_1 = input("Enter Num_1:")
num_2 = input("Enter Num_2:")

#converting them to integers
num_1 = int(num_1)
num_2 = int(num_2)

#printing their sum
sum = num_1 + num_2
print(sum)

#printing their difference
difference = num_1 - num_2
print(difference)

#printing their product
product = num_1*num_2
print(product)

#finding equality
if num_1 > num_2:
 print("Num_1 is greater than Num_2")

elif num_1 == num_2:
 print("Num_1 is equal to Num_2")

else :
 print("Num_1 is lesser than Num_2")
