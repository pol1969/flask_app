nobel_winners = [  
        {'category': 'Physics',  'name': 'Albert Einstein',  'nationality': 'Swiss',  'sex': 'male',  'year': 1921},  
        {'category': 'Physics',  'name': 'Paul Dirac',  'nationality': 'British',  'sex': 'male',  'year': 1933},  
        {'category': 'Chemistry',  'name': 'Marie Curie',  'nationality': 'Polish',  'sex': 'female',  'year': 1911} 
        ]

import csv  
with open('data/nobel_winners.csv', 'w') as f:  
    fieldnames = nobel_winners[0].keys() 
    sorted(fieldnames) 
    writer = csv.DictWriter(f, fieldnames=fieldnames)  
    writer.writeheader() 
    for w in nobel_winners:  
        writer.writerow(w) 

with open('data/nobel_winners.csv') as f:  
    reader = csv.reader(f)  
    for row in reader: 
        print(row)
