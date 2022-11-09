from flask import Flask, jsonify
import sqlite3


app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('sitio.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_query_data(query_string):
    conn = get_db_connection()
    query = conn.execute(query_string).fetchall()

    items_array = []
    for row in query:
        row_dict = dict(row)
        for column in row_dict:
            #The field 'password' of some user can't be serializable.
            if isinstance(row_dict[column], bytes):
                row_dict[column] = row_dict[column].decode()
        items_array.append(row_dict)

    conn.close()
    return items_array


@app.route("/proyecto/<id_proyecto>")
def proyecto(id_proyecto):

    projects_query_string = f"SELECT * FROM project WHERE project_name LIKE '%{id_proyecto}%'"
    proyectos = get_query_data(projects_query_string)

    #If we want all the users that don't have role, we have to add 'OUTER LEFT JOIN' 
    users_query_string = """
        SELECT * FROM user
        JOIN user_role_association_table
            ON user.id = user_role_association_table.user_id
        JOIN role
            ON user_role_association_table.role_id = role.id
    """
    usuarios = get_query_data(users_query_string)

    response_data = {"projects": proyectos, "users": usuarios}
    response = jsonify(response_data)
    return response


if __name__ == "__main__":
    app.run()