 #Create a program that prints the multiplication table of a given number using a while loop. 
num=int(input("enter a number"))
i=1
while i<11:
    result=num*i
    print(f"{num} X {i}={result}")
    i=i+1
