from flask import Flask, render_template, request, redirect, session
from users import User
app = Flask(__name__) 

# homepage, READ from the database, display on frontend
@app.route('/') 
def index():
    return render_template("index.html", users = User.get_all())

# add new user form page, CREATE new user
@app.route('/new') 
def add_new():
    return render_template("new.html")

# CREATE new user, POST form data
@app.route('/new', methods=['POST']) 
def add_new_form():
    User.create_one(request.form)
    return redirect("/") 

# UPDATE current user form page 
@app.route('/update/<int:id>') 
def add_new(id):
    # continuing writing this out
    return render_template("update.html")

# UPDATE current user, POST form data
@app.route('/update', methods=['POST']) 
def add_new_form():
    User.update_one(request.form)
    return redirect("/") 

if __name__=="__main__": 
    app.run(debug=True) 

