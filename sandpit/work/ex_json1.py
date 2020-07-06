
nobel_winners = [  
        {'category': 'Physics',  'name': 'Albert Einstein',  'nationality': 'Swiss',  'sex': 'male',  'year': 1921},  
        {'category': 'Physics',  'name': 'Paul Dirac',  'nationality': 'British',  'sex': 'male',  'year': 1933},  
        {'category': 'Chemistry',  'name': 'Marie Curie',  'nationality': 'Polish',  'sex': 'female',  'year': 1911} 
        ]
import json  

with open('data/nobel_winners.json', 'w') as f:  
    json.dump(nobel_winners, f)  
    
open('data/nobel_winners.json').read()
