#Buzz number
n = int(input("Enter a number : "))
if n % 7 == 0 or n / 7 == 0 :
    print (f"{n} is a Buzz number")
else :
    print (f"{n} is NOT a Buzz number")