from flask_restx import Namespace, Resource
import company_dao as company

ns = Namespace('company', description='Companies operations')

@ns.route('/add_company')
class AddCompany(Resource):
    def post(self):
        return company.add_company()

@ns.route('/get_company/<int:com_id>')
class GetCompany(Resource):
    def get(self, com_id):
        return company.get_company(com_id)

@ns.route('/get_all_companies')
class GetAllCompanies(Resource):
    def get(self):
        return company.get_all_companies()

@ns.route('/update_company/<int:com_id>')
class UpdateCompany(Resource):
    def put(self, com_id):
        return company.update_company(com_id)

@ns.route('/delete_company/<int:com_id>')
class DeleteCompany(Resource):
    def delete(self, com_id):
        return company.delete_company(com_id)