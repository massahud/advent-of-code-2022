# define a function to calculate the total score
def get_total_score(rounds):
    total_score = 0
    # map each choice to its corresponding score
    choice_scores = {"X": 1, "Y": 2, "Z": 3}
    # map each outcome to the corresponding shape
    outcome_shapes = {"X": "R", "Y": "S", "Z": "P"}
    
    for round in rounds:
        opponent_choice = round[0]
        outcome = round[1]
        
        # calculate the shape the player should choose
        player_choice = outcome_shapes[outcome]
        
        # calculate the score for the shape the player chose
        shape_score = choice_scores[player_choice]
        
        # calculate the score for the outcome of the round
        if (opponent_choice == "A" and player_choice == "Y") or (opponent_choice == "B" and player_choice == "Z") or (opponent_choice == "C" and player_choice == "X"):
            outcome_score = 6
        elif (opponent_choice == "A" and player_choice == "Z") or (opponent_choice == "B" and player_choice == "X") or (opponent_choice == "C" and player_choice == "Y"):
            outcome_score = 0
        else:
            outcome_score = 3
        
        # add the scores to the total
        total_score += shape_score + outcome_score
    
    return total_score

# read the rounds from the input file
rounds = []
with open("input.txt", "r") as file:
    for line in file:
        opponent_choice, outcome = line.strip().split()
        rounds.append((opponent_choice, outcome))

# calculate and print the total score
total_score = get_total_score(rounds)
print(total_score)
