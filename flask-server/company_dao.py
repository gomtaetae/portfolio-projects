from flask import request, jsonify, render_template
import db_connection as db

def add_company():
    connection = db.create_connection()
    cursor = connection.cursor()
    com_name = request.json['com_name']
    head_address = request.json['head_address']
    phone = request.json['phone']
    cursor.callproc('company_management_pkg.addCompany', [com_name, head_address, phone])
    connection.commit()
    return jsonify({"status": "success"}), 201

def get_company(com_id):
    connection = db.create_connection()
    cursor = connection.cursor()
    com_ref_cursor = cursor.callfunc('company_management_pkg.getCompany', db.CURSOR, [com_id])
    com_data = []
    for row in com_ref_cursor:
        row_as_dict = {desc[0]: value for desc, value in zip(com_ref_cursor.description, row)}
        com_data.append(row_as_dict)
    return jsonify(com_data)

def get_all_companies():
    connection = db.create_connection()
    cursor = connection.cursor()
    com_ref_cursor = cursor.callfunc('company_management_pkg.getAllCompanies', db.CURSOR)
    com_data = []
    for row in com_ref_cursor:
        row_as_dict = {desc[0]: value for desc, value in zip(com_ref_cursor.description, row)}
        com_data.append(row_as_dict)
    return jsonify(com_data)

def get_all_companies_html():
    connection = db.create_connection()    
    cursor = connection.cursor()
    com_ref_cursor = cursor.callfunc('company_management_pkg.getAllCompanies', db.CURSOR)
    coms_data = []
    for row in com_ref_cursor:
        row_as_dict = {desc[0]: value for desc, value in zip(com_ref_cursor.description, row)}
        coms_data.append(row_as_dict)
    return render_template('all_company.html', coms=coms_data)


def update_company(com_id):
    connection = db.create_connection()
    cursor = connection.cursor()
    com_name = request.json['com_name']
    head_address = request.json['head_address']
    phone = request.json['phone']
    cursor.callproc('company_management_pkg.updateCompany', [com_id, com_name, head_address, phone])
    connection.commit()
    return jsonify({"status": "updated"}), 200

def delete_company(com_id):
    connection = db.create_connection()
    cursor = connection.cursor()
    cursor.callproc('company_management_pkg.deleteCompany', [com_id])
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify(message='Company deleted successfully')