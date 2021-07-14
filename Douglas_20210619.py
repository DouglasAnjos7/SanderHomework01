vid_games = ["Playstation", "Xbox", "Switch"]                           #Question 2
print(vid_games)                                                        #Question 3

for vid_game in vid_games:                                              #Question 4
    print(vid_game)                                                     #Question 5
    print(vid_game)

for vid_game in vid_games:                                              #Question 6
    print(vid_game.upper())                                               

print("This is my list:")                                               #Question 7
for vid_game in vid_games:                                              
    print(vid_game)
                    
for vid_game in vid_games:                                              #Question 8
    print(vid_game)
print("This was my list")

for vid_game in vid_games:                                              #Question 9
    print("This is one item of my list: " + vid_game)

for vid_game in vid_games:                                              #Question 10
    print(vid_game + " This was one item of my list")

number_list = []                                                        #Question 11
for value in range(2,24):
    values = value
    number_list.append(values)
    print(value)
print(number_list)

list12 = list(range(11,24,3))                                           #Question 12
print(list12)                                                           #Question 13

my_list = []                                                            #Question 14  
total = 1
for value_1 in range(0,6):
    total = total + value_1
    my_list.append(total)
print(my_list)                                                          

fruit_list = ["orange","banana","blueberry","melon","strawberry"]       #Question 15
print(fruit_list)                                                       #Question 16
print(fruit_list[0:3])                                                  #Question 17
print(fruit_list[2:5])                                                  #Question 18
print(fruit_list[1:5])                                                  #Question 19
print(fruit_list[1:5])                                                  #Question 20
print(sorted(fruit_list[1:5], reverse=True))                            #Question 21

for fruit in fruit_list[0:5:2]:
    print(fruit)