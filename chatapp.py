import os
from flask import Flask, redirect, render_template, request

app = Flask (__name__)

# stores messages btw requests
messages = []

banned_words = [
        'cat',
        'ass',
        'fuck',
        'Cats'
    
    ]
#Creating rooms
# @app.route('rooms/add')
# def add_room():
#     roomname = request.form['roomname']
#     rooms[roomname] = []
#     return redirect(....)
    
@app.route("/")
def get_index():
    return render_template("index.html")
    
    
    
    
    
@app.route("/login")
def login():
    username = request.args.get('username')
    return redirect(username) 


@app.route("/<username>")
def get_username(username):
    return render_template("chat.html", logged_in_as=username, all_the_messages=messages)
  
@app.route("/new", methods=["POST"])
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
    
    
    
    
    
    
    
    
    
    
   
    

    
if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
# app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)  
    
