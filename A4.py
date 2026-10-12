A=int(input("Enter bit A:"))
B=int(input("Enter bit B:"))
if (A==0 or A==1) and (B==0 or B==1):
  print("AND=",A and B)
  print(" OR=",A| B)
  print ("XOR=",A^B)
else:
    print("Bits must be 0 or 1")


   
