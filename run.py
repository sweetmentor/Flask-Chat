import os
from flask import Flask, redirect, render_template, request

app = Flask (__name__)

# stores messages btw requests
messages = []

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
    
@app.route("/<username>/new", methods=["POST"])
def add_message(username):
    text = request.form['message']
    message = {
        'sender': username,
        'body' : text
    }
    
    messages.append(message)
    return redirect(username) 
    

    
    
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)  
    
