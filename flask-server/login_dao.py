from flask import request, jsonify
import db_connection as db

def login_user():
    connection = db.create_connection()
    cursor = connection.cursor()
    user_name = request.json['user_name']
    birthyear = request.json['birthyear']
    print(user_name)
    cursor.execute(
        "SELECT COUNT(*) FROM med_user WHERE user_name = :user_name AND birthyear = :birthyear",
        user_name=user_name,
        birthyear=birthyear
    )

    
    count = cursor.fetchone()[0]
    
    if count == 1:
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"status": "failure"}), 401