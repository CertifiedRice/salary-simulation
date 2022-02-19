# 1.5 seconds = 1 year
# 1 dollar = 1k dollars
# not a good salary I know lol ;)
# customize the program if you wish! Send an issue showcasing your cool adjustments if you want to :)

import time

people = ['John', 'Paul', 'George']

salary = {'John': 100, 'Paul': 200, 'George': 300}

wallet = {'John': 100, 'Paul': 200, 'George': 300}

for i in range(0, 3):
    print(people[i])
    print(salary[people[i]])
    print(wallet[people[i]])
    wallet[people[i]] += salary[people[i]]
    print(wallet)
    time.sleep(1.5)