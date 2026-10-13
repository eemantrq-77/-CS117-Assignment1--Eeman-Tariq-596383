Readings =(3.3,3.1,3.4,2.9,3.6,3.0,3.2)
count=0
total=0
highest=Readings[0]
lowest=Readings[0]
for i in range (len(Readings)):
    if Readings [i] > 3.2:
        count+=1
    if Readings [i]>highest:
        highest=Readings[i]
    if Readings[i]<lowest:
        lowest=Readings[i]
    total+=Readings[i]
average=total/len(Readings)
print("Readings above 3.2V:",count)
print("Highest:",highest,"V")
print("Lowest:",lowest,"V")
print("Average:",round(average,2),"V")

