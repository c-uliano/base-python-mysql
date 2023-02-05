from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User

# ? --------------------------------------
# READ all users, display on frontend
@app.route('/') 
def index():
    return render_template("read.html", users = User.get_all())  
# ? --------------------------------------



# ? --------------------------------------
# add new user form page
@app.route('/add/user') 
def add_user():
    return render_template("create.html")  

# CREATE new user, POST data
@app.route('/create/user', methods=['POST']) 
def create_user():
    User.save(request.form)

    return redirect('/') 
# ? --------------------------------------



# ? --------------------------------------
# READ one user, show on frontend in filled-out form
@app.route('/update/user/<int:id>') 
def update_user(id):   
    data = { 
        "id": id # id key, matches the column in the database, the name of the hidden input in the form
    }

    return render_template("update.html", user = User.get_one(data))  

# UPDATE user, collect form data
# need hidden input on the form with the user id
@app.route('/update/user', methods=['POST']) 
def update_user_form():
    User.update_one(request.form)

    return redirect("/")  
# ? --------------------------------------



# ? --------------------------------------
# READ user, show on frontend
@app.route('/view/user/<int:id>') 
def view_user(id):
    data = { 
        "id": id # id, the column in the database
    }

    return render_template("view.html", user = User.get_one(data))  
# ? --------------------------------------



# ? --------------------------------------
# DELETE user
@app.route('/delete/user/<int:id>') 
def delete_user(id):

    data ={ 
        "id": id # id, the column in the database
    }

    User.remove_one(data)

    return redirect("/")  
# ? --------------------------------------
