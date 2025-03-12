import random

def get_random_temp(season):
   
    if season == "winter":
        return round(random.uniform(-10, 16), 1)
    elif season == "spring":
        return round(random.uniform(5, 23), 1)
    elif season == "summer":
        return round(random.uniform(18, 40), 1)
    elif season == "autumn" or season == "fall":
        return round(random.uniform(5, 25), 1)
    else:
        return round(random.uniform(-10, 40), 1)  

def get_season_from_month(month):
    
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return "summer"
    elif month in [9, 10, 11]:
        return "autumn"

def main():
    
   
    month = int(input("Enter the month number (1-12): "))
    
    season = get_season_from_month(month)
    
    
    temp = get_random_temp(season)
   
    print(f"\nThe temperature right now is {temp}°C.")
    
    
    if temp < 0:
        print("That’s freezing! Wear extra layers today.")
    elif 0 <= temp < 16:
        print(" Quite chilly! Don’t forget your coat.")
    elif 16 <= temp < 23:
        print(" Pleasant weather! Enjoy your day.")
    elif 23 <= temp < 32:
        print(" Warm weather! Stay hydrated.")
    else:
        print(" It's really hot! Stay cool and drink plenty of water.")


main()
