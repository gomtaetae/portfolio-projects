from flask import Flask
from flask_restx import Api, Resource
from flask_cors import CORS
import users_dao as med_user

app = Flask(__name__)
CORS(app, origins="*")

# 문제 : https://github.com/python-restx/flask-restx/issues/523
# 해결 : https://github.com/noirbizarre/flask-restplus/issues/712#issuecomment-957444231
     
@app.route("/")
def welcome():
    return "Welcome!"

api = Api(app, version='1.0', title='My App API',
          description='A simple My App API',
          doc='/api/')

@api.route('/add_user')
class AddUser(Resource):
    def post(self):
        return med_user.add_user()

@api.route('/get_user/<int:user_id>')
class GetUser(Resource):
    def get(self, user_id):
        return med_user.get_user(user_id)

@api.route('/get_all_users')
class GetAllUsers(Resource):
    def get(self):
        return med_user.get_all_users()

@api.route('/get_all_users_html')
class GetAllUsersHTML(Resource):
    def get(self):
        return med_user.get_all_users_html()

@api.route('/update_user/<int:user_id>')
class UpdateUser(Resource):
    def put(self, user_id):
        return med_user.update_user(user_id)

@api.route('/delete_user/<int:user_id>')
class DeleteUser(Resource):
    def delete(self, user_id):
        return med_user.delete_user(user_id)


if __name__ == '__main__':
    app.run(port=5002, debug=True)