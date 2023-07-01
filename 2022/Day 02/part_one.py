from get_data import playbook

player_moves_score: dict[str, int] = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}
moves: dict[str, str] = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
}

# should probably make a dictionary for this, but I am too lazy for now
# win = 6
# draw = 3
# loss = 0

score: int = 0
for play in playbook:
    player_move: str = moves[play[1]]
    opponent_move: str = moves[play[0]]
    # add score for our move choice
    score += player_moves_score[player_move]
    # then check the outcome of the round and add score
    if player_move == opponent_move:
        score += 3
    elif player_move == "rock" and opponent_move == "scissors":
        score += 6
    elif player_move == "paper" and opponent_move == "rock":
        score += 6
    elif player_move == "scissors" and opponent_move == "paper":
        score += 6

print(score)
