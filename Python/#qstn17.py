#Creating a list with 8 random integers between 1–100
import random

nums = [random.randint(1, 100) for _ in range(8)]

#Finding and printing the biggest number and the smallest number
big = nums[0]
small = nums[0]

for n in nums:
    if n > big:
        big = n
    if n < small:
        small = n

print("List:", nums)
print("Biggest:", big)
print("Smallest:", small)