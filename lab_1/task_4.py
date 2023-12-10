users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

site_visit = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
site_visit["Общее количество"] = len(users)
site_visit["Уникальные посещения"] = len(set(users))

print(site_visit)
