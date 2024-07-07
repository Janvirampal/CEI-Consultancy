#Create a program that checks if a given year is a leap year. 
def check_leap(year):
    if((year%400==0) or (year%100!=0) and (year%4==0)):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

year=int(input("enter year"))
check_leap(year)