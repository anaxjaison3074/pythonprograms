n = int (input ("Enter the year: "))
if(n % 400 - 0) :
    print ("Year is leap Year")
elif ((n % 100 - 0) and (n % 400 != 0)):
    print ("Year is not a leap year")
elif(n% 4 == 0) :
    print ("Year is a leap year")
else:
    print ("NOT A LEAP YEAR")
