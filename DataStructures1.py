# Data Structures ============================================================================================

# 'int' is a class, use help(int) to read about it.

shoplist = ['apple', 'mango', 'carrot', 'banana']
shoplist2= ['loki', 'thor','cap', 'walker']
print('I have', len(shoplist), 'items to purchase.')    # finding length
print('These items are:', end=' ')
for item in shoplist:
    print(item, end=' ')                # printing all list items
print('\nI also have to buy rice.')
shoplist.append('rice')                 # adding an item in already existing list
print('My shopping list is now', shoplist)
print('I will sort my list now')
shoplist.sort()                     # sorting items of a list
print('Sorted shopping list is', shoplist)
print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]             # deleting a list item.
print('I bought the', olditem)
print('My shopping list is now', shoplist)
print('\n'*2)

shoplist.append(shoplist2);     # Can add a list by itself.

print("Print shoplist using only the name : ", shoplist)
print("Print older shoplist which is not part of new one but kept its identity : ", shoplist[4])
# prints all that was in older list on just giving the address of old list as it exists inside new one.
print("Print the last element which is already part of another list : ", shoplist[4][3])

#print("Print the last element : ", shoplist[7]) # This will not work as the last element is part of a nested list.

print('\n'*2)
# for..in loop to iterate through the items of the list. =================

# List is also a sequence ===================

# Tuple example ==============================================================================================

# I would recommend always using parentheses
# to indicate start and end of tuple
# even though parentheses are optional.
# Explicit is better than implicit.

zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))
new_zoo = 'monkey', 'camel', zoo
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',
    len(new_zoo)-1+len(new_zoo[2]))


# a tuple within a tuple does not lose its identity. =====================
# ====================================

#Dictionary ======================================================================

