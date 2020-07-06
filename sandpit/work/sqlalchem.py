nobel_winners = [  
        {'category': 'Physics',  'name': 'Albert Einstein',  'nationality': 'Swiss',  'sex': 'male',  'year': 1921},  
        {'category': 'Physics',  'name': 'Paul Dirac',  'nationality': 'British',  'sex': 'male',  'year': 1933},  
        {'category': 'Chemistry',  'name': 'Marie Curie',  'nationality': 'Polish',  'sex': 'female',  'year': 1911} 
        ]


from sqlalchemy import create_engine  

engine = create_engine(  'sqlite:///data/nobel_prize.db', echo=True)

from sqlalchemy.ext.declarative import declarative_base  
Base = declarative_base()

#Example 3-3. Defining an SQL database table 
from sqlalchemy import Column, Integer, String, Enum 

class Winner(Base):  
    __tablename__ = 'winners'   
    id = Column(Integer, primary_key=True)  
    name = Column(String)  
    category = Column(String)  
    year = Column(Integer)  
    nationality = Column(String)  
    sex = Column(Enum('male', 'female'))   
    
    def __repr__(self):  
        return "<Winner(name='%s', category='%s', year='%s')>"%(self.name, self.category, self.year)

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker  
Session = sessionmaker(bind=engine) 
session = Session()

albert = Winner(**nobel_winners[0]) 
session.add(albert) 
session.new

session.expunge(albert) 
session.new

winner_rows = [Winner(**w) for w in nobel_winners] 
session.add_all(winner_rows) 
session.commit()

#Example 3-4. Converts an SQLAlchemy instance to a dict 
def inst_to_dict(inst, delete_id=True):  
    dat = {}  
    for column in inst.__table__.columns: 
        dat[column.name] = getattr(inst, column.name)  
    
    if delete_id:  
        dat.pop('id') 
    
    return dat

winner_rows = session.query(Winner) 
nobel_winners = [inst_to_dict(w) for w in winner_rows] 
print(nobel_winners)
