from flask import request, jsonify, render_template
import db_connection as db

def add_medicine():
    connection = db.create_connection()
    cursor = connection.cursor()
    ingredient = request.json['ingredient']
    med_name = request.json['med_name']
    price = request.json['price']
    company = request.json['company']
    deadline = request.json['deadline']
    keepmethod = request.json['keepmethod']
    intakemethod = request.json['intakemethod']
    intakewarn = request.json['intakewarn']
    shape = request.json['shape']
    cursor.callproc('medicine_management_pkg.addMedicine', [ingredient, med_name, price, company, deadline, keepmethod, intakemethod, intakewarn, shape])
    connection.commit()
    return jsonify({"status": "success"}), 201

def get_medicine(med_id):
    connection = db.create_connection()
    cursor = connection.cursor()
    med_ref_cursor = cursor.callfunc('medicine_management_pkg.getMedicine', db.CURSOR, [med_id])
    med_data = []
    for row in med_ref_cursor:
        row_as_dict = {desc[0]: value for desc, value in zip(med_ref_cursor.description, row)}
        med_data.append(row_as_dict)
    return jsonify(med_data)

def get_all_medicines():
    connection = db.create_connection()
    cursor = connection.cursor()
    med_ref_cursor = cursor.callfunc('medicine_management_pkg.getAllMedicines', db.CURSOR)
    med_data = []
    for row in med_ref_cursor:
        row_as_dict = {desc[0]: value for desc, value in zip(med_ref_cursor.description, row)}
        med_data.append(row_as_dict)
    return jsonify(med_data)

def get_all_medicines_html():
    connection = db.create_connection()    
    cursor = connection.cursor()
    medicines_ref_cursor = cursor.callfunc('medicine_management_pkg.getAllMedicines', db.CURSOR)
    medicines_data = []
    for row in medicines_ref_cursor:
        row_as_dict = {desc[0]: value for desc, value in zip(medicines_ref_cursor.description, row)}
        medicines_data.append(row_as_dict)
    return render_template('all_medicine.html', medicines=medicines_data)

def update_medicine(med_id):
    connection = db.create_connection()
    cursor = connection.cursor()
    ingredient = request.json['ingredient']
    med_name = request.json['med_name']
    price = request.json['price']
    company = request.json['company']
    deadline = request.json['deadline']
    keepmethod = request.json['keepmethod']
    intakemethod = request.json['intakemethod']
    intakewarn = request.json['intakewarn']
    shape = request.json['shape']
    cursor.callproc('medicine_management_pkg.updateMedicine', [med_id, ingredient, med_name, price, company, deadline, keepmethod, intakemethod, intakewarn, shape])
    connection.commit()
    return jsonify({"status": "updated"}), 200

def delete_medicine(med_id):
    connection = db.create_connection()
    cursor = connection.cursor()
    cursor.callproc('medicine_management_pkg.deleteMedicine', [med_id])
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify(message='Medicine deleted successfully')