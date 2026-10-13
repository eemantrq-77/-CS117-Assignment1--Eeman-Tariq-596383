r=int(input("Enter the number of resistors used in series:"))
total=0
for i in range (1,r+1):
    R=float(input("Enter R"+ str(i) +":"))
    total=total+R
    
print("Total resistance is:",total)

