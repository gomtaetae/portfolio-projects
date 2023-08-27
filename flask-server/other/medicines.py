from flask_restx import Namespace, Resource
import medicine_dao as medicine

ns = Namespace('medicine', description='Medicines operations')

@ns.route('/add_medicine')
class AddMedicine(Resource):
    def post(self):
        return medicine.add_medicine()

@ns.route('/get_medicine/<int:med_id>')
class GetMedicine(Resource):
    def get(self, med_id):
        return medicine.get_medicine(med_id)

@ns.route('/get_all_medicines')
class GetAllMedicines(Resource):
    def get(self):
        return medicine.get_all_medicines()

@ns.route('/update_medicine/<int:med_id>')
class UpdateMedicine(Resource):
    def put(self, med_id):
        return medicine.update_medicine(med_id)

@ns.route('/delete_medicine/<int:med_id>')
class DeleteMedicine(Resource):
    def delete(self, med_id):
        return medicine.delete_medicine(med_id)