from flask import Flask, render_template, request, redirect, session
from users import User
app = Flask(__name__) 

# homepage, READ from the database, display on frontend
@app.route('/') 
def index():
    return render_template("index.html", users = User.get_all())


# ? These work together ------------
# add new user form page
@app.route('/new') 
def add_new():
    return render_template("new.html")

# CREATE new user, POST form data
@app.route('/new', methods=['POST']) 
def add_new_form():
    User.create_one(request.form)
    return redirect("/") 
# ? -----------------------


# READ one user, display on frontend
@app.route('/new/<int:id>') 
def view_one(id):
    data = {
        "id" : id
    }
    
    return render_template("view.html", user = User.view_one(data))


# ? These work together ------------
# READ one user, display on frontend, update user form page 
@app.route('/update/<int:id>') 
def update_one(id):
    data = {
        "id" : id
    }

    return render_template("update.html", user = User.view_one(data))

# UPDATE current user, POST form data
# ! this form needs to have the hidden input for id
@app.route('/update', methods=['POST']) 
def add_new_form():
    User.update_one(request.form)
    return redirect("/") 
# ? -----------------------


if __name__=="__main__": 
    app.run(debug=True) 

