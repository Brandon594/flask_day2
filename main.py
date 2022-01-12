from flask import Flask

#this will work in CMD, comment out if using browser
username = input("Enter User's Name:")

app = Flask(__name__)

@app.route("/main")
def home():
    return "<h1>This is the main page.<h1>"

@app.route("/user")
def user(username):
    return f"<h1>user:{username}<h1>"

@app.route("/about")
def about():
    return "<h1>This is the about page<h1>"


if __name__ =="__main__":
    app.run()

#CMD prompts:
#Command to run program: flask_day_2\python "main.py"
#URL generated:(use/ & route to access page) http://127.0.0.1:5000/
#http://127.0.0.1:5000/main
