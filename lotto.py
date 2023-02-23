import random
lottery_numbers = set(random.sample(list(range(22)), 6))
print(lottery_numbers)
# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 22, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
]

for player in players:
  player_numbers = (player["numbers"])
  # print(player_numbers)
  numbers_matched = lottery_numbers.intersection(player_numbers)
  print(player["name"], numbers_matched, len(numbers_matched))

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)