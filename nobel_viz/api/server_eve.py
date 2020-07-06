# api/server_eve.py 
# testing http http://127.0.0.1:5000/api/winners_cleaned\?where='{"country":"Russia"}'

from eve import Eve  

app = Eve()  

if __name__=='__main__':  
    app.run(debug=True)
