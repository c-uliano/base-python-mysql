from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



# ? --------------------------------------
    # READ all users, display on frontend
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("users_schema").query_db(query)

        users = []

        for user in results:
            users.append(cls(user))
        
        return users
# ? --------------------------------------



# ? --------------------------------------
    # CREATE new user, add form data to database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, NOW(), NOW());"

        return connectToMySQL("users_schema").query_db(query, data)
# ? --------------------------------------



# ? --------------------------------------
    # READ one user, show on frontend
    @classmethod
    def get_one(cls, data):
        query  = "SELECT * FROM users WHERE id = %(id)s;" # * id, matching the table column
        result = connectToMySQL('users_schema').query_db(query, data)

        return cls(result[0]) # ! is this making an object out of the first result from the database? I think it is.
# ? --------------------------------------



# ? --------------------------------------
    # UPDATE user with form data
    @classmethod
    def update_one(cls, data):
        query  = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;" # * id, matching the table column

        return connectToMySQL('users_schema').query_db(query, data)
# ? --------------------------------------



# ? --------------------------------------
    # DELETE user
    @classmethod
    def remove_one(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"

        return connectToMySQL('users_schema').query_db(query, data)
# ? --------------------------------------

