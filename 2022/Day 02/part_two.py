from get_data import playbook

player_moves_score: dict[str, int] = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}
round_outcome_score: dict[str, int] = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}
moves: dict[str, str] = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
}

score: int = 0
for play in playbook:
    opponent_move: str = moves[play[0]]
    player_move: str = play[1]
    # we already know if we are going to win from the playbook, so we can add the scores now
    score += round_outcome_score[player_move]
    if player_move.lower() == "y":
        score += player_moves_score[opponent_move]
    # rock
    elif opponent_move == "rock" and player_move.lower() == "x":
        score += player_moves_score["scissors"]
    elif opponent_move == "rock" and player_move.lower() == "z":
        score += player_moves_score["paper"]
    # paper
    elif opponent_move == "paper" and player_move.lower() == "x":
        score += player_moves_score["rock"]
    elif opponent_move == "paper" and player_move.lower() == "z":
        score += player_moves_score["scissors"]
    # scissors
    elif opponent_move == "scissors" and player_move.lower() == "x":
        score += player_moves_score["paper"]
    elif opponent_move == "scissors" and player_move.lower() == "z":
        score += player_moves_score["rock"]

print(score)
