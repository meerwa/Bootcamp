
my_fav_numbers = {7, 13, 21}  
my_fav_numbers.update({42, 99})  
my_fav_numbers.remove(max(my_fav_numbers))  

friend_fav_numbers = {5, 14, 21}  

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)  
print(our_fav_numbers)
