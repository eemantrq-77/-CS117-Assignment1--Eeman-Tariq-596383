Voltage=int(input("Enter voltage in volts:"))      #taking input from user
Resistance=int(input("Enter resistance in ohms:"))
current=Voltage/Resistance                         #using arithmetic operators
if current>2:                                      #using if/else statement
 print("Fuse will blow")
else:
    print("Circuit is safe")
