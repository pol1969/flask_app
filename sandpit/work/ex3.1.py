nobel_winners = [  
        {'category': 'Physics',  'name': 'Albert Einstein',  'nationality': 'Swiss',  'sex': 'male',  'year': 1921},  
        {'category': 'Physics',  'name': 'Paul Dirac',  'nationality': 'British',  'sex': 'male',  'year': 1933},  
        {'category': 'Chemistry',  'name': 'Marie Curie',  'nationality': 'Polish',  'sex': 'female',  'year': 1911} 
        ]

f = open('data/nobel_winners.csv', 'w')

cols = nobel_winners[0].keys() 
sorted(cols)
with open('data/nobel_winners.csv', 'w') as f: 
    f.write(','.join(cols) + '\n') 
    
    for o in nobel_winners:  
        row = [str(o[col]) for col in cols] 
        f.write(','.join(row) + '\n')

with open('data/nobel_winners.csv') as f:  
    for line in f.readlines():  
        print(line),
