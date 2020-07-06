from pymongo import MongoClient  
import pandas as pd



def get_mongo_database(db_name, host='localhost',  port=27017, username=None, password=None):  
    """ Get named database from MongoDB with/out authentication """  
    # make Mongo connection with/out authentication  
    if username and password:  
        mongo_uri = 'mongodb://%s:%s@%s/%s'% (username, password, host, db_name)  
        conn = MongoClient(mongo_uri)  
    else:  
        conn = MongoClient(host, port)

    return conn[db_name]

def mongo_coll_to_dicts(dbname='test', collname='test',  query={}, del_id=True, **kw): 
    db = get_mongo_database(dbname, **kw)  
    res = list(db[collname].find(query))   
    if del_id:  
        for r in res:  
            r.pop('_id')   
    return res


def dataframe_to_mongo(df, db_name, collection, host='localhost', port=27017, username=None, password=None):  
    """ save a dataframe to mongodb collection """  
    db = get_mongo_database(db_name, host, port, username,  password)   
    records = df.to_dict('records')  
    db[collection].insert_many(records)

def mongo_to_dataframe(db_name, collection, query={}, host='localhost', port=27017, username=None, password=None, no_id=True):  
    """ create a dataframe from mongodb collection """   
    db = get_mongo_database(db_name, host, port, username, password)   
    cursor = db[collection].find(query)   
    df = pd.DataFrame(list(cursor))   
    if no_id: 
        del df['_id']   
    return df

