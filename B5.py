one_percent = 0
five_percent = 0
reject = 0

R = float(input("Enter measured resistance (0 to stop): "))

while R != 0:
    if 99.0 <= R <= 101.0:
        one_percent = one_percent + 1

    elif 95.0 <= R <= 105.0:
        five_percent = five_percent + 1

    else:
        reject = reject + 1

    R = float(input("Enter measured resistance (0 to stop): "))

print("1% tolerance resistors:", one_percent)
print("5% tolerance resistors:", five_percent)
print("Rejected resistors:", reject)
