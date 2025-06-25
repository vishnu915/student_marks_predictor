from flask import Flask, render_template, request
import pickle
import mysql.connector

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vishnu@123",
    database="student_prediction"
)
cursor = db.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    name = request.form['name']
    roll = request.form['roll']
    hours = float(request.form['hours'])

    predicted_marks = model.predict([[hours]])[0]

    cursor.execute("INSERT INTO students (name, roll_no, hours_studied, predicted_marks) VALUES (%s, %s, %s, %s)",
                   (name, roll, hours, predicted_marks))
    db.commit()

    return render_template('result.html', name=name, roll=roll, hours=hours, marks=round(predicted_marks, 2))

if __name__ == "__main__":
    app.run(debug=True)