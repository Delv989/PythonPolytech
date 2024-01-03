def find_common_participants(first, second, separator=","):
    unique_participants1 = set(first.split(separator))
    unique_participants2 = set(second.split(separator))

    common_participants = list(unique_participants1.intersection(unique_participants2))
    common_participants.sort()

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

find_common_participants(participants_first_group, participants_second_group, "|")
