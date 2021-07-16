five_fruits = ["orange","banana","strawberry","melon","kiwi"]           #Question 2
newref_fruits = five_fruits                                             #Question 3
newref_fruits.append("water melon")                                     #Question 4
print(newref_fruits)                                                    #Question 5
print(five_fruits)

#Question 6: Because when we create a reference, all properties are changed to all instances

slc_fruits = five_fruits[0:6]                                           #Question 7
del slc_fruits[1]                                                       #Question 8
print(slc_fruits)                                                       #Question 9
print(five_fruits)

#Question 10: Because the slice action copy the choosen range to the new list.

the_tuple = (20, 5, 254)                                                #Question 11
for number in the_tuple:                                                #Question 12
    print(number)
#the_tuple[0] = 150                                                     #Question 13 no, because tuple list can't be 
the_tuple = (68, 89)                                                    #Question 14
print(the_tuple)

for numbers in range(1,11):                                             #Question 15
    print(numbers)

for numbers in range(1,11):                                             #Question 16
    if numbers > 5:
        print(numbers)

for numbers in range(1,11):                                             #Question 17
    if numbers <= 3:
        print(numbers)

for numbers in range(1,11):                                             #Question 18
    if numbers == 4 or numbers > 8:
        print(numbers)

for numbers in range(1,11):                                             #Question 19
    if numbers > 3 and numbers < 6:
        print(numbers)

twenth_list = [2,4,6,8,10,12]                                           #Question 20
for number in range(10):                                                #Question 21
    if number in twenth_list:
        print(number)

for number in range(10):                                                #Question 21
    if number in twenth_list:
        print(number)

oranges = 146                                                           #Question 22
if oranges < 100:
    print("Buy more oranges!")
else:
    print("You have oranges enough!")

for numbers in range(11):                                               #Question 23 and 24
    if numbers > 8:
        print("There was at least one number bigger than 8")
    else:
        print("There were no numbers bigger than 8")