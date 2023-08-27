from flask import request, jsonify, render_template
import db_connection as db

def add_user():
    connection = db.create_connection()
    cursor = connection.cursor()
    user_name = request.json['user_name']
    birthyear = request.json['birthyear']
    birthday = request.json['birthday']
    gender = request.json['gender']
    cursor.callproc('users_management_pkg.addUser', [user_name, birthyear, birthday, gender])
    connection.commit()
    return jsonify({"status": "success"}), 201


def get_user(user_id):
    connection = db.create_connection()
    cursor = connection.cursor()
    user_ref_cursor = cursor.callfunc('users_management_pkg.getUser', db.CURSOR, [user_id])
    user_data = []
    for row in user_ref_cursor:
        row_as_dict = {desc[0]: value for desc, value in zip(user_ref_cursor.description, row)}
        user_data.append(row_as_dict)
    return jsonify(user_data)


def get_all_users():
    connection = db.create_connection()    
    cursor = connection.cursor()
    users_ref_cursor = cursor.callfunc('users_management_pkg.getAllUsers', db.CURSOR)
    users_data = []
    for row in users_ref_cursor:
        row_as_dict = {desc[0]: value for desc, value in zip(users_ref_cursor.description, row)}
        users_data.append(row_as_dict)
    return jsonify(users_data)


def get_all_users_html():
    connection = db.create_connection()    
    cursor = connection.cursor()
    users_ref_cursor = cursor.callfunc('users_management_pkg.getAllUsers', db.CURSOR)
    users_data = []
    for row in users_ref_cursor:
        row_as_dict = {desc[0]: value for desc, value in zip(users_ref_cursor.description, row)}
        users_data.append(row_as_dict)
    return render_template('all_users.html', users=users_data)


def update_user(user_id):
    connection = db.create_connection() 
    cursor = connection.cursor()
    user_name = request.json['user_name']
    birthyear = request.json['birthyear']
    birthday = request.json['birthday']
    gender = request.json['gender']
    cursor.callproc('users_Package.updateUser', [user_id, user_name, birthyear, birthday, gender])
    connection.commit()
    return jsonify({"status": "updated"}), 200


def delete_user(user_id):
    connection = db.create_connection()
    cursor = connection.cursor()
    cursor.callproc('users_management_pkg.deleteUser', [user_id])
    connection.commit()
    cursor.close()
    connection.close()

    return jsonify(message='User deleted successfully')



