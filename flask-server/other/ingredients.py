from flask_restx import Namespace, Resource
import ingredient_dao as ingredient

ns = Namespace('ingredient', description='Ingredients operations')

@ns.route('/add_ingredient')
class AddIngredient(Resource):
    def post(self):
        return ingredient.add_ingredient()

@ns.route('/get_ingredient/<int:ing_id>')
class GetIngredient(Resource):
    def get(self, ing_id):
        return ingredient.get_ingredient(ing_id)

@ns.route('/get_all_ingredients')
class GetAllIngredients(Resource):
    def get(self):
        return ingredient.get_all_ingredients()

@ns.route('/update_ingredient/<int:ing_id>')
class UpdateIngredient(Resource):
    def put(self, ing_id):
        return ingredient.update_ingredient(ing_id)

@ns.route('/delete_ingredient/<int:ing_id>')
class DeleteIngredient(Resource):
    def delete(self, ing_id):
        return ingredient.delete_ingredient(ing_id)