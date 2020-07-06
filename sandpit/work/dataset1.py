nobel_winners = [  
        {'category': 'Physics',  'name': 'Albert Einstein',  'nationality': 'Swiss',  'sex': 'male',  'year': 1921},  
        {'category': 'Physics',  'name': 'Paul Dirac',  'nationality': 'British',  'sex': 'male',  'year': 1933},  
        {'category': 'Chemistry',  'name': 'Marie Curie',  'nationality': 'Polish',  'sex': 'female',  'year': 1911} 
        ]



import dataset  
db = dataset.connect('sqlite:///data/nobel_prize.db')

wtable = db['winners'] 
winners = wtable.find() 
winners = list(winners)
print(winners)

wtable = db['winners'] 
wtable.drop()  
wtable = db['winners'] 
wtable.find()

with db as tx: 
    for w in nobel_winners:  
        tx['winners'].insert(w)

print(list(db['winners'].find()))   

from datafreeze import freeze

winners = db['winners'].find() 
freeze(winners, format='csv',filename='data/nobel_winners_ds.csv')
open('data/nobel_winners_ds.csv').read()
