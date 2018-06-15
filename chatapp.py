import os
from datetime import datetime
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

messages = []

banned_words = [
        'cat',
        'ass',
        'fuck',
        'Cats'
    
    ]


def write_to_file(filename, data):
    """Handle the process of writing data to a file"""
    with open(filename, "a") as file:
        file.writelines(data)


def add_messages(username, message):
    """Add messages to the `messages` text file"""
    write_to_file("data/messages.txt", "({0}) {1} - {2}\n".format(
            datetime.now().strftime("%H:%M:%S"),
            username.title(),
            message))


def get_all_messages():
    """Get all of the messages and separate them by a `br`"""
    messages = []
    with open("data/messages.txt", "r") as chat_messages:
        messages = chat_messages.readlines()
    return messages


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        write_to_file("data/users.txt", request.form["username"] + "\n")
        return redirect(request.form["username"])
    return render_template("index.html")




@app.route('/<username>')
def user(username):
    """Display chat messages"""
    if request.method == "POST":
        add_messages(username, request.form["message"] + "\n")
    
    
    messages = get_all_messages()
    return render_template("chat.html", username=username, chat_messages=messages)


@app.route('/new')
def add_message():
    username = request.form['username']
    text = request.form['message']

    words = text.split()       # Banning bad words
    words = [ "*" * len(word) if word.lower() in banned_words else word for word in words]
    
    text = " ".join(map(str,words))
    
    # for i in range(len(words)):  #banning bad words
    #     for j in range(len(banned_words)):
    #         if words[i].lower() == banned_words[j]:
    #             words[i] = "*" * len(words[i])
                
   
    # for word in words:
    #     if word.lower() in banned_words:
    #         word = "*" * len(words[i])
    
    # for banned_words in banned_words: 
    #     text = text.replace(" " + banned_words + " ", "*" len(banned_words))
    
    message = {
        'sender': username,
        'body': text,
    }
    
    messages.append(message)
    return redirect(username)

app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)











