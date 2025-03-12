family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

for name, age in family.items():
    if age < 3:
        ticket_price = 0 
    elif 3 <= age <= 12:
        ticket_price = 10  
    else:
        ticket_price = 15  
    
    total_cost += ticket_price
    print(f"{name} (Age {age}): ${ticket_price}")


print(f"Total cost for the family: ${total_cost}")
