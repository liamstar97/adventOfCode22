"""
Rock paper scissors
-
Key:
Player  1 2
        A Y
        B X
        C Z

Rock = A X
Paper = B Y
Scissors = C Z

Scores:
Rock = 1
Paper = 2
Scissors = 3
Loss = 0
Draw = 3
Win = 6
-
Goal: Determine the total score of player 2 after every round has been completed
"""
from typing import Callable

# dict that contains strategy guide for winning plays
strategy_dict = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

# dict for scoring play outcomes with shape score
shape_score_dict = {'rock': 1, 'paper': 2, 'scissors': 3}


def decrypt_play(play):
    # dict that contains shape names based on encryption
    decode_plays_dict = {('A', 'X'): 'rock', ('B', 'Y'): 'paper', ('C', 'Z'): 'scissors'}
    return next(value for key, value in decode_plays_dict.items() if play in key)


def calculate_part1_score(player1_outcome, player2_outcome) -> int:
    player2_shape_score = shape_score_dict[player2_outcome]

    # if outcome is a draw
    if player1_outcome == player2_outcome:
        return player2_shape_score + 3

    # if outcome is a win
    if player1_outcome == strategy_dict[player2_outcome]:
        return player2_shape_score + 6

    # else outcome is a loss
    return player2_shape_score


def calculate_part2_score(player1_outcome, player2_outcome) -> int:
    encoded_outcomes_dict = {'rock': 'lose', 'paper': 'draw', 'scissors': 'win'}

    # if win is necessary then find winning play and calculate total
    if encoded_outcomes_dict[player2_outcome] == 'win':
        winning_play = next(key for key, value in strategy_dict.items() if player1_outcome == value)
        return shape_score_dict[winning_play] + 6

    # if loss in necessary then find loosing play and calculate total
    if encoded_outcomes_dict[player2_outcome] == 'lose':
        losing_play = strategy_dict[player1_outcome]
        return shape_score_dict[losing_play] + 0

    # else play is a draw
    return shape_score_dict[player1_outcome] + 3


def calculate_round_score(player1: str, player2: str, calculate_score: Callable) -> int:
    # determine outcome from encoded play
    player1_outcome = decrypt_play(player1)
    player2_outcome = decrypt_play(player2)
    return calculate_score(player1_outcome, player2_outcome)


def play_rpc(file_name: str, calculate_score: Callable) -> int:
    total_score = 0
    with open(file_name) as file:
        for _round in file.readlines():
            # split on whitespace and remove newline char
            plays = list(map(lambda s: s.strip('\n'), _round.rsplit(' ')))
            round_score = calculate_round_score(plays[0], plays[1], calculate_score)
            total_score += round_score
    return total_score


if __name__ == '__main__':
    print('---part1---')
    print(play_rpc('data/day2', calculate_part1_score))
    print(play_rpc('data/day2mock', calculate_part1_score))
    print('---part2---')
    print(play_rpc('data/day2', calculate_part2_score))
    print(play_rpc('data/day2mock', calculate_part2_score))
