list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

count_team = 2
count_players = len(list_players)
divider = count_players//count_team

first_team = list_players[:divider]
second_team = list_players[divider:]

print(first_team)
print(second_team)