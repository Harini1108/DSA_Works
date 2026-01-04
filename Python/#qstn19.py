#creating list
grades = [85, 92, 78, 65, 88, 91, 73, 89, 55, 94]


#Counting how many students:
#got A (≥90)
#got B (80–89)
#got C (70–79)
#got below 70

A = B = C = below = 0

for g in grades:
    if g >= 90:
        A += 1
    elif g >= 80:
        B += 1
    elif g >= 70:
        C += 1
    else:
        below += 1

print("A:", A)
print("B:", B)
print("C:", C)
print("Below 70:", below)