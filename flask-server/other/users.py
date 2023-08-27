from flask_restx import Namespace, Resource
import users_dao as users

ns = Namespace('users', description='Users operations')

@ns.route('/add_user')
class AddUser(Resource):
    def post(self):
        return users.add_user()

@ns.route('/get_user/<int:user_id>')
class GetUser(Resource):
    def get(self, user_id):
        return users.get_user(user_id)

@ns.route('/get_all_users')
class GetAllUsers(Resource):
    def get(self):
        return users.get_all_users()

@ns.route('/get_all_users_html')
class GetAllUsersHTML(Resource):
    def get(self):
        return users.get_all_users_html()

@ns.route('/update_user/<int:user_id>')
class UpdateUser(Resource):
    def put(self, user_id):
        return users.update_user(user_id)

@ns.route('/delete_user/<int:user_id>')
class DeleteUser(Resource):
    def delete(self, user_id):
        return users.delete_user(user_id)