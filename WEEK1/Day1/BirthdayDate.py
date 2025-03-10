from datetime import datetime

# Ask the user for their birthdate
birthdate = input("Enter your birthdate (DD/MM/YYYY): ")

# Extract the birth year and calculate the age
day, month, year = map(int, birthdate.split('/'))
current_year = datetime.now().year
age = current_year - year


candles = age % 10  

# Check if it's a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    is_leap = True
else:
    is_leap = False

# Function to print the birthday cake
def print_cake(candles):
    print(f"   __{'i' * candles}__")
    print("  |:H:a:p:p:y:|")
    print("__|___________|__")
    print("|^^^^^^^^^^^^^^^|")
    print("|:B:i:r:t:h:d:a:y:|")
    print("|                 |")
    print("~~~~~~~~~~~~~~~~~~~")

# Print the cake(s)
if is_leap:
    print("\n🎉 You were born in a leap year! Two cakes for you! 🎉\n")
    print_cake(candles)
    print()
    print_cake(candles)
else:
    print_cake(candles)
