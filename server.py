from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def start_guess():
    return "<h1>Guess a number between 0 and 9</h1>" \
        "<img src = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

rand_num = random.randint(1,10)
@app.route("/URL/<user_guess>")
def check_num(user_guess):
    user_guess = int(user_guess)
    print(rand_num)
    print(user_guess)
    if(user_guess < rand_num):
        return "<h1 style='color:red'>Too low, Try again</h1>" \
                         "<img src = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif (user_guess > rand_num):
         return "<h1 style='color:purple'>Too High, Try again</h1>" \
             "<img src = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h1 style='color:green'>You found me</h1>" \
             "<img src = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    
if __name__ == "__main__":
    app.run(debug=True)