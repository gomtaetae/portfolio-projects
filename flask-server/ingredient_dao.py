from flask import request, jsonify, render_template
import db_connection as db

def add_ingredient():
    connection = db.create_connection()
    cursor = connection.cursor()
    ing_name = request.json['ing_name']
    purpose1 = request.json['purpose1']
    purpose2 = request.json['purpose2']
    good = request.json['good']
    bad = request.json['bad']
    rec_age = request.json['rec_age']
    rec_intaketime = request.json['rec_intaketime']
    user_ch_choose_id = request.json['user_ch_choose_id']
    cursor.callproc('ingredient_management_pkg.addIngredient', [ing_name, purpose1, purpose2, good, bad, rec_age, rec_intaketime, user_ch_choose_id])
    connection.commit()
    return jsonify({"status": "success"}), 201

def get_ingredient(ing_id):
    connection = db.create_connection()
    cursor = connection.cursor()
    ing_ref_cursor = cursor.callfunc('ingredient_management_pkg.get ', db.CURSOR, [ing_id])
    ing_data = []
    for row in ing_ref_cursor:
        row_as_dict = {desc[0]: value for desc, value in zip(ing_ref_cursor.description, row)}
        ing_data.append(row_as_dict)
    return jsonify(ing_data)

def get_all_ingredients():
    connection = db.create_connection()
    cursor = connection.cursor()
    ing_ref_cursor = cursor.callfunc('ingredient_management_pkg.getAllIngredients', db.CURSOR)
    ing_data = []
    for row in ing_ref_cursor:
        row_as_dict = {desc[0]: value for desc, value in zip(ing_ref_cursor.description, row)}
        ing_data.append(row_as_dict)
    return jsonify(ing_data)

def get_all_ingredients_html():
    connection = db.create_connection()    
    cursor = connection.cursor()
    ingredient_ref_cursor = cursor.callfunc('ingredient_management_pkg.getAllIngredients', db.CURSOR)
    ingredient_data = []
    for row in ingredient_ref_cursor:
        row_as_dict = {desc[0]: value for desc, value in zip(ingredient_ref_cursor.description, row)}
        ingredient_data.append(row_as_dict)
    return render_template('all_ingredient.html', ingredients=ingredient_data)

def update_ingredient(ing_id):
    connection = db.create_connection()
    cursor = connection.cursor()
    ing_name = request.json['ing_name']
    purpose1 = request.json['purpose1']
    purpose2 = request.json['purpose2']
    good = request.json['good']
    bad = request.json['bad']
    rec_age = request.json['rec_age']
    rec_intaketime = request.json['rec_intaketime']
    user_ch_choose_id = request.json['user_ch_choose_id']
    cursor.callproc('ingredient_management_pkg.updateIngredient', [ing_id, ing_name, purpose1, purpose2, good, bad, rec_age, rec_intaketime, user_ch_choose_id])
    connection.commit()
    return jsonify({"status": "updated"}), 200

def delete_ingredient(ing_id):
    connection = db.create_connection()
    cursor = connection.cursor()
    cursor.callproc('ingredient_management_pkg.deleteIngredient', [ing_id])
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify(message='Ingredient deleted successfully')
