import os


for i in range(1,19):
    d = str(i) + ' day ago'
    with open('hack.txt', 'a') as file:
        file.write(d)
    os.system('git add bot.txt')
    os.system('git commit --date="' + d + '" -m "first commit"')
os.system('git push -u origin master')