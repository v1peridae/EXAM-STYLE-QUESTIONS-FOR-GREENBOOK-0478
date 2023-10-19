player_one_point = 0
player_two_point = 0

player_one_name = input("Input player one name")
player_two_name = input("Input player two name")


for i in range(0, 7):
    print("There are 4 possible moves \nCat \nLion \nHorse \nElephant")
    player_one_move = input("P1 - Pick a move:")
    player_two_move = input("P2 - Pick a move:")

    if player_one_move == "Elephant" and player_two_move == "Lion" or player_one_move == "Lion" and player_two_move == "Horse" or player_one_move == "Cat" and player_two_move == "Elephant" or player_one_move == "Horse" and player_two_move == "Cat":
        player_one_point = player_one_point + 1

    elif player_two_move == "Elephant" and player_one_move == "Lion" or player_two_move == "Lion" and player_one_move == "Horse" or player_two_move == "Cat" and player_one_move == "Elephant" or player_two_move == "Horse" and player_one_move == "Cat":
        player_two_point = player_two_point + 1

if player_one_point > player_two_point:
    winner = player_one_name
elif player_two_point > player_one_point:
    winner = player_two_name

print("Player one has", player_one_point)
print("Player two has", player_two_point)

print("The winner is:", winner)
