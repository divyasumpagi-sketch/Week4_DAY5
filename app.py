from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Abhi@83119",
    database="college_db"
)

cursor = db.cursor()

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    query = "SELECT * FROM Users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    if user:
        return redirect("/success")
    else:
        return "Login Failed! Invalid Username or Password"

@app.route("/success")
def success():
    return "Login Successful!"

    print(username)
    print(password)

if __name__ == "__main__":
    app.run(debug=True)