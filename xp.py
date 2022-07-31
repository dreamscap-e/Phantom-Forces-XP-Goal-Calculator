current_xp = int(input('Please enter your current xp: '))
desired_level = int(input('Please enter the level you would like to rank up to: '))
desired_xp = 0
for level in range(desired_level):
    xp = (level + 1) * 1000
    desired_xp += xp
xp_needed = desired_xp - current_xp
print('You need', xp_needed, 'more xp.')
remaining = open('remaining.txt', 'w')
remaining.write(str(xp_needed))
remaining.close()
