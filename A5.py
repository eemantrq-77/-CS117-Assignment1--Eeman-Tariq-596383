r1=int(input("Enter value of resistor 1:"))
r2=int(input("Enter value of resistor 2:"))
r3=int(input("Enter value of resistor 3:"))
if r1 <= r2 and r1 <= r3:
    smallest = r1
elif r2 <= r1 and r2 <= r3:
    smallest = r2
else:
    smallest = r3

if r1 >= r2 and r1 >= r3:
    largest = r1
elif r2 >= r1 and r2 >= r3:
    largest = r2
else:
    largest = r3

print("Smallest resistor =", smallest)
print("Largest resistor =", largest)
