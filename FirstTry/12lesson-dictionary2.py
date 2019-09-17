#     key  :  value
enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Mudila',
    'awards': ['Zvezda Gitlera', 'Zvezda Stalina',],
    'image': ['image1','image2','image3'],
}

all_enemies = []
for x in range(0,10):
    all_enemies.append(enemy.copy()) # если добавлять без copy то каждый индекс в массиве будет залинкован друг с другом и словарем

for enem in all_enemies:
    print(enem)
print('+++++++++++++++')
all_enemies[4]['health'] = 30
all_enemies[1]['name'] = 'Kozel'
all_enemies[0]['loc_x'] += 10
for enem in all_enemies:
    print(enem)