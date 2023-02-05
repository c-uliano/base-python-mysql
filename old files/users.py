from mysqlconnection import MySQLConnection

class User:
    def __init__(self, data):
        # update properties according to database
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # READ all the data in the database, display on frontend
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM table_name_here;"
        results = MySQLConnection("database_name_here").query_db(query)

        users = []

        for user in results:
            users.append(cls(user))

        return users

    # CREATE a new user
    @classmethod
    def create_one(cls, data):
        query = "INSERT INTO table_name_here (column_one, column_two, created_at, updated_at) VALUES (%(form_input_name_one)s, %(form_input_name_two)s, NOW(), NOW())"
        return MySQLConnection("database_name_here").query_db(query, data)

    # READ data for one user, display on frontend
    @classmethod
    def view_one(cls):
        pass

    # UPDATE data for one user
    @classmethod
    def update_one(cls, data):
        query = "UPDATE table_name_here SET column1 = value1 column2 = value2 WHERE id = %(id)s;"

        return MySQLConnection("database_name_here").query_db(query, data)

    # DELETE data for one user
    @classmethod
    def delete_one(cls):
        pass