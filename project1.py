import random
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll
while True:
    player = input("enter the number of player(2 to 4): ")
    if player.isdigit():
        player = int(player)
        if 2<=player<=4:
            break
        else:
            print("Enter between 2 to 4")
    else:
        print("Enter valid numbers")
max_score = 50
player_score = [0 for _ in range(player)]
while True:
    for i in range(player):
        print("Your number", i+1, "turn. has started")
        current_score = 0
        while True:
            should_roll = input("You want roll dice(y): ")
            if should_roll.lower() != "y":
                break
            value = roll()
            if value == 1:
                print("you got 1 so Your turn is over")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
            print("Your current score is :", current_score)
        player_score[i] = current_score
        print("Your total score is:", player_score[i])
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)

