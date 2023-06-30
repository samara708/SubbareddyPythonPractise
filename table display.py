tableInput=int(input("enter the  number"))
startingNumber=int(input("enter the starting  number"))
endingNumber=int(input("enter the ending number "))
for i in range(startingNumber,endingNumber+1):
    mul=tableInput*i
    print(tableInput,"*",i,"=",mul)