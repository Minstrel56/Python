#     key  :  value
enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'healt': 100,
    'name': 'Mudila',
}
print(enemy)
print("Location X = "+str(enemy['loc_x']))
print("Location Y = "+str(enemy['loc_y']))
print("His name is "+enemy['name'])

enemy['rank'] = 'Admiral'
print(enemy)

del enemy['rank']
print(enemy)

enemy['loc_x'] = enemy['loc_x'] + 40
enemy['healt'] = enemy['healt'] - 30
if enemy['healt'] < 80:
    enemy['color'] = 'yellow'

print(enemy)

print(enemy.keys())
print(enemy.values())