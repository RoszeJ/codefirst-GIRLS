empty_list = []
list_of_numbers = [0, 1, 2, 3, 4, 5]
my_favorite_fruits = ['pineapples','oranges','bananas']
mixed_list = [15,'sunsihine','jumper',4,'sky']

list_combined = ['list_of_numbers','my_favorite_fruits','mixed_list']
print(list_combined)

pick_list = raw_input()
if pick_list in list_combined: 
  if pick_list == 'list_of_numbers':
   print(list_of_numbers)
   pick = raw_input('0 to 5 \n')
   pick = int(pick)
   print(list_of_numbers[pick])
  if pick_list == 'my_favorite_fruits': 
   print(my_favorite_fruits)
   pick = raw_input('0 to 2 \n')
   pick = int(pick)
   print(my_favorite_fruits[pick])
  if pick_list == 'mixed_list': 
   print(mixed_list)
   pick = raw_input('0 to 4 \n')
   pick = int(pick)
   print(mixed_list[pick])
  