# The script counts if the year is leap or not.

year = int(input("Enter a year: "))

def is_leap_year(year):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print ("The year is leap")
  else:
    print("The year is not leap")

is_leap_year(year)