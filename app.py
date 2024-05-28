from flask import Flask, request, jsonify
import joblib
import numpy as np 
import psycopg2 
import os


model = joblib.load('model.joblib')
app = Flask(__name__)



def get_db_connection():

    conn = psycopg2.connect(
    dbname="mydatabase",
    user="myuser",
    password="mypassword",
    host="127.0.0.1"
    port = "5430"
    )
    return conn

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict(np.array(data['features']).reshape(1, -1))
    result = int(prediction[0])

    # Store prediction in the database
    conn = get_db_connection()
    cur = conn.cursor()


    
    cur.execute("""
    INSERT INTO predictions (features)
    VALUES (%s)
""", (result,))
    

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)

    






