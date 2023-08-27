from flask import Flask
from flask_cors import CORS
import users_dao as users
import company_dao as company
import ingredient_dao as ingredient
import medicine_dao as medicine
import login_dao as login_user
# import purpose_dao as user_purpose

app = Flask(__name__)
CORS(app, origins="*")

# @app.route('/')

# login_dao routers
# @app.route('/login', methods=['POST'])
# def login():
#     return login_user()

# users_dao routes
app.add_url_rule('/add_user', view_func=users.add_user, methods=['POST'])
app.add_url_rule('/get_user/<int:user_id>', view_func=users.get_user, methods=['GET'])
app.add_url_rule('/get_all_users', view_func=users.get_all_users, methods=['GET'])
app.add_url_rule('/get_all_users_html', view_func=users.get_all_users_html, methods=['GET'])
app.add_url_rule('/update_user/<int:user_id>', view_func=users.update_user, methods=['PUT'])
app.add_url_rule('/delet_user/<int:user_id>', view_func=users.delete_user, methods=['DELETE'])
app.add_url_rule('/login_user', view_func=login_user.login_user, methods=['POST'])

# #purpose_dao routes
# app.add_url_rule('/get_purpose/<int:user_id>', view_func=user_purpose.get_purpose, methods=['GET'])
# app.add_url_rule('/get_all_purposes', view_func=user_purpose.get_all_purposes, methods=['GET'])
# app.add_url_rule('/get_all_purposes_html', view_func=user_purpose.get_all_purposes_html, methods=['GET'])
# app.add_url_rule('/update_purpose/<int:user_id>', view_func=user_purpose.update_purpose, methods=['PUT'])
# app.add_url_rule('/delet_purpose/<int:user_id>', view_func=user_purpose.delete_purpose, methods=['DELETE'])

# company_dao routes
app.add_url_rule('/add_company', view_func=company.add_company, methods=['POST'])
app.add_url_rule('/get_company/<int:com_id>', view_func=company.get_company, methods=['GET'])
app.add_url_rule('/get_all_companies', view_func=company.get_all_companies, methods=['GET'])
app.add_url_rule('/get_all_companies_html', view_func=company.get_all_companies_html, methods=['GET'])
app.add_url_rule('/update_company/<int:com_id>', view_func=company.update_company, methods=['PUT'])
app.add_url_rule('/delete_company/<int:com_id>', view_func=company.delete_company, methods=['DELETE'])

# ingredient_dao routes
app.add_url_rule('/add_ingredient', view_func=ingredient.add_ingredient, methods=['POST'])
app.add_url_rule('/get_ingredient/<int:ing_id>', view_func=ingredient.get_ingredient, methods=['GET'])
app.add_url_rule('/get_all_ingredients', view_func=ingredient.get_all_ingredients, methods=['GET'])
app.add_url_rule('/get_all_ingredients_html', view_func=ingredient.get_all_ingredients_html, methods=['GET'])
app.add_url_rule('/update_ingredient/<int:ing_id>', view_func=ingredient.update_ingredient, methods=['PUT'])
app.add_url_rule('/delete_ingredient/<int:ing_id>', view_func=ingredient.delete_ingredient, methods=['DELETE'])

# medicine_dao routes
app.add_url_rule('/add_medicine', view_func=medicine.add_medicine, methods=['POST'])
app.add_url_rule('/get_medicine/<int:med_id>', view_func=medicine.get_medicine, methods=['GET'])
app.add_url_rule('/get_all_medicines', view_func=medicine.get_all_medicines, methods=['GET'])
app.add_url_rule('/get_all_medicines_html', view_func=medicine.get_all_medicines_html, methods=['GET'])
app.add_url_rule('/update_medicine/<int:med_id>', view_func=medicine.update_medicine, methods=['PUT'])
app.add_url_rule('/delete_medicine/<int:med_id>', view_func=medicine.delete_medicine, methods=['DELETE'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    
    
